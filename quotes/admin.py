# quotes/admin.py

from django.contrib import admin, messages
from django import forms
from django.db import models
from .models import Quote, Program, ProgramItem, EventType, Package, QuoteHistory
from .views import generate_tracking_code # Import the function
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active', 'order')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')
    list_editable = ('order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')

class ProgramItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProgramItem
    extra = 1
    fields = ('repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']

@admin.action(description='Clonar programas seleccionados')
def clone_programs(modeladmin, request, queryset):
    for program in queryset:
        original_pk = program.pk
        original_items = list(ProgramItem.objects.filter(program_id=original_pk))
        program.pk = None
        program.name = f"Copia de {program.name}"
        program.save()
        items_to_clone = [ProgramItem(program=program, repertoire_piece=item.repertoire_piece, position=item.position) for item in original_items]
        ProgramItem.objects.bulk_create(items_to_clone)
    modeladmin.message_user(request, f"{queryset.count()} programas han sido clonados.", messages.SUCCESS)

@admin.register(Program)
class ProgramAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProgramItemInline]
    list_display = ('name', 'piece_count')
    search_fields = ['name']
    list_display_links = ('name',)
    actions = [clone_programs]
    @admin.display(description='Nº Piezas')
    def piece_count(self, obj):
        return obj.items.count()

class QuoteHistoryInline(admin.TabularInline):
    model = QuoteHistory
    extra = 0
    readonly_fields = ('user', 'timestamp', 'action')
    can_delete = False
    def has_add_permission(self, request, obj=None): return False

class QuoteAdminForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        widgets = { 'event_address': forms.Textarea(attrs={'rows': 4}), }

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    form = QuoteAdminForm
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost', 'paid_amount', 'balance_due')
    list_filter = ('status', 'event_type', 'event_date', 'created_by_source')
    search_fields = ('tracking_code', 'client_name', 'client_email', 'event_address', 'program__name')
    # UPDATED: Removed raw_id_fields to revert to a simple dropdown
    # raw_id_fields = ('program',) 
    readonly_fields = (
        'tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user',
        'total_cost', 'payment_per_musician', 'cost_musicians_base', 'cost_weekend_fee', 
        'cost_distance_fee', 'cost_gala_fee', 'cost_primetime_fee', 'cost_manager_base',
        'cost_manager_per_person', 'cost_manager_exterior', 'cost_manager_boda', 'cost_car_fee',
        'total_musician_payout_rounded', 'balance_due', 'calculation_log'
    )
    inlines = [QuoteHistoryInline]

    fieldsets = (
        ('Información General', { 'fields': ('tracking_code', 'client_name', 'status', 'event_type', 'package', 'program') }),
        ('Detalles del Evento', { 'fields': ('event_date', 'event_time', 'location_type', 'event_address', 'is_exterior', 'dress_code') }),
        ('Agrupación (si no se usa paquete)', { 'fields': ('num_voices', 'num_musicians') }),
        ('Pago y Costo', { 'fields': ('paid_amount', 'discount', 'total_cost', 'balance_due', 'payment_per_musician') }),
        ('Contacto del Cliente', { 'fields': ('client_email', 'client_phone', 'contact_method', 'comments') }),
        ('Costos Detallados (Solo Lectura)', {
            'classes': ('collapse',),
            'fields': (
                'cost_musicians_base', 'total_musician_payout_rounded', 'cost_weekend_fee', 'cost_distance_fee', 
                'cost_gala_fee', 'cost_primetime_fee', 'cost_manager_base', 'cost_manager_per_person', 
                'cost_manager_exterior', 'cost_manager_boda', 'cost_car_fee', 'calculation_log'
            )
        }),
        ('Información de Creación (Solo Lectura)', { 'classes': ('collapse',), 'fields': ('created_by_source', 'created_by_user', 'created_at', 'updated_at') }),
    )

    @admin.display(description='Saldo Pendiente')
    def balance_due(self, obj):
        return f"${obj.total_cost - obj.paid_amount:,.2f} MXN"

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing
        
        original_obj = None
        if change: original_obj = Quote.objects.get(pk=obj.pk)

        if not obj.tracking_code:
            obj.tracking_code = generate_tracking_code()

        pricing_breakdown, calculation_log_str = calculate_pricing(obj)
        obj.calculation_log = calculation_log_str 
        for key, value in pricing_breakdown.items():
            setattr(obj, key, value)

        if not obj.pk: obj.created_by_source = Quote.CreatedSource.ADMIN
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)

        if change and original_obj:
            changes = []
            changed_fields = form.changed_data[:] 
            if 'status' in changed_fields:
                changes.append(f"Estado cambiado de '{original_obj.get_status_display()}' a '{obj.get_status_display()}'")
                changed_fields.remove('status')
            for field_name in changed_fields:
                try:
                    field = obj._meta.get_field(field_name)
                    verbose_name = field.verbose_name
                    old_val = getattr(original_obj, field_name)
                    if hasattr(field, 'choices') and field.choices:
                         old_val = dict(field.choices).get(old_val, old_val)
                    changes.append(f"'{verbose_name}' cambiado de '{old_val}' a '{form.cleaned_data[field_name]}'")
                except (forms.Field.DoesNotExist, AttributeError): pass
            if changes:
                QuoteHistory.objects.create(user=request.user, quote=obj, action="; ".join(changes))
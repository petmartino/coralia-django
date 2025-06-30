# quotes/admin.py

from django.contrib import admin
from django import forms
from django.db import models
from .models import Quote, Program, ProgramItem, EventType, Package, QuoteHistory
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register the new Package model
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active',)


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')
    list_editable = ('order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')


class ProgramItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProgramItem
    extra = 1
    fields = ('repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']

# UPDATED: Re-added SortableAdminMixin and specified list_display_links
@admin.register(Program)
class ProgramAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProgramItemInline]
    list_display = ('__str__', 'quote_tracking_code', 'piece_count')
    search_fields = ['name', 'quote__tracking_code']
    # This forces the first column (__str__) to be a clickable link.
    list_display_links = ('__str__',)

    @admin.display(description='Quote ID')
    def quote_tracking_code(self, obj):
        # Check for obj.quote existence before accessing tracking_code
        if hasattr(obj, 'quote') and obj.quote:
            return obj.quote.tracking_code
        return "N/A"
    
    @admin.display(description='Nº Piezas')
    def piece_count(self, obj):
        return obj.items.count()

# NEW: History inline for the Quote admin
class QuoteHistoryInline(admin.TabularInline):
    model = QuoteHistory
    extra = 0
    readonly_fields = ('user', 'timestamp', 'action')
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

# NEW: Custom form to control widgets in QuoteAdmin
class QuoteAdminForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        widgets = {
            'event_address': forms.Textarea(attrs={'rows': 4}),
        }

# Greatly enhanced QuoteAdmin
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    form = QuoteAdminForm  # Use the custom form
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost', 'paid_amount', 'balance_due')
    list_filter = ('status', 'event_type', 'event_date', 'created_by_source')
    search_fields = ('tracking_code', 'client_name', 'client_email', 'event_address')
    readonly_fields = (
        'tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user',
        'total_cost', 'payment_per_musician', 'cost_musicians_base', 'cost_weekend_fee', 
        'cost_distance_fee', 'cost_gala_fee', 'cost_primetime_fee', 'cost_manager_base',
        'cost_manager_per_person', 'cost_manager_exterior', 'cost_manager_boda', 'cost_car_fee',
        'total_musician_payout_rounded', 'balance_due'
    )
    inlines = [QuoteHistoryInline]

    fieldsets = (
        ('Información General', {
            'fields': ('tracking_code', 'client_name', 'status', 'event_type', 'package', 'program')
        }),
        ('Detalles del Evento', {
            'fields': ('event_date', 'event_time', 'location_type', 'event_address', 'is_exterior', 'dress_code'),
        }),
        ('Agrupación (si no se usa paquete)', {
            'fields': ('num_voices', 'num_musicians')
        }),
        ('Pago y Costo', {
            'fields': ('paid_amount', 'discount', 'total_cost', 'balance_due', 'payment_per_musician')
        }),
        ('Contacto del Cliente', {
            'fields': ('client_email', 'client_phone', 'contact_method', 'comments')
        }),
        ('Costos Detallados (Solo Lectura)', {
            'classes': ('collapse',),
            'fields': ('cost_musicians_base', 'total_musician_payout_rounded', 'cost_weekend_fee',
                       'cost_distance_fee', 'cost_gala_fee', 'cost_primetime_fee',
                       'cost_manager_base', 'cost_manager_per_person', 'cost_manager_exterior',
                       'cost_manager_boda', 'cost_car_fee')
        }),
        ('Información de Creación (Solo Lectura)', {
            'classes': ('collapse',),
            'fields': ('created_by_source', 'created_by_user', 'created_at', 'updated_at')
        }),
    )

    @admin.display(description='Saldo Pendiente')
    def balance_due(self, obj):
        balance = obj.total_cost - obj.paid_amount
        return f"${balance:,.2f} MXN"

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing
        
        original_obj = None
        if change:
            original_obj = Quote.objects.get(pk=obj.pk)

        pricing_breakdown = calculate_pricing(obj)
        for key, value in pricing_breakdown.items():
            setattr(obj, key, value)

        if not obj.pk: 
            obj.created_by_source = Quote.CreatedSource.ADMIN
        
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)

        if change and original_obj:
            changes = []
            changed_fields = form.changed_data
            if 'status' in changed_fields:
                old_status = original_obj.get_status_display()
                new_status = obj.get_status_display()
                changes.append(f"Estado cambiado de '{old_status}' a '{new_status}'")
                if 'status' in changed_fields: changed_fields.remove('status') # prevent duplication

            for field in changed_fields:
                old_val = getattr(original_obj, field)
                new_val = getattr(obj, field)
                # Ensure verbose_name exists to prevent errors on system fields
                try:
                    verbose_name = obj._meta.get_field(field).verbose_name
                except Exception:
                    verbose_name = field
                changes.append(f"'{verbose_name}' cambiado de '{old_val}' a '{new_val}'")

            if changes:
                QuoteHistory.objects.create(
                    quote=obj,
                    user=request.user,
                    action="; ".join(changes)
                )
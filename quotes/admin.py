# quotes/admin.py

from django.contrib import admin
from .models import Quote, Program, ProgramItem, EventType, Package, QuoteHistory # <-- Import new models
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register the new Package model
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')
    list_editable = ('order', 'is_funeral_type', 'has_wedding_fee', 'manager_base_fee')


class ProgramItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProgramItem
    extra = 1
    fields = ('repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']

# UPDATED: Remove SortableAdminMixin to fix the error and disable sorting.
@admin.register(Program)
class ProgramAdmin(SortableAdminMixin, admin.ModelAdmin): # <--- REMOVED SortableAdminMixin
    inlines = [ProgramItemInline]
    list_display = ('__str__', 'quote_tracking_code', 'piece_count')
    search_fields = ['name', 'quote__tracking_code']

    # This allows you to edit the name directly in the list view
    list_display_links = ('name',)

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

# Greatly enhanced QuoteAdmin
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost', 'paid_amount')
    list_filter = ('status', 'event_type', 'event_date', 'created_by_source')
    search_fields = ('tracking_code', 'client_name', 'client_email', 'event_address')
    # Make all cost fields readonly to enforce recalculation
    readonly_fields = (
        'tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user',
        'total_cost', 'payment_per_musician', 'cost_musicians_base', 'cost_weekend_fee', 
        'cost_distance_fee', 'cost_gala_fee', 'cost_primetime_fee', 'cost_manager_base',
        'cost_manager_per_person', 'cost_manager_exterior', 'cost_manager_boda', 'cost_car_fee',
        'total_musician_payout_rounded'
    )
    inlines = [QuoteHistoryInline] # <-- ADD HISTORY

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
            'fields': ('paid_amount', 'discount', 'total_cost', 'payment_per_musician')
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

    # UPDATED save_model to include recalculation and history tracking
    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing  # We'll move pricing logic to a utility function
        
        original_obj = None
        if change:
            original_obj = Quote.objects.get(pk=obj.pk)

        # Recalculate pricing
        pricing_breakdown = calculate_pricing(obj) # Pass the whole object
        for key, value in pricing_breakdown.items():
            setattr(obj, key, value) # Update the object with new calculated values

        # When a quote is saved in the admin, set the source to ADMIN if it's new
        if not obj.pk: 
            obj.created_by_source = Quote.CreatedSource.ADMIN
        
        # Always update the user who last saved it
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)

        # Track changes
        if change and original_obj:
            changes = []
            for field in form.changed_data:
                old_val = getattr(original_obj, field)
                new_val = getattr(obj, field)
                changes.append(f"'{field}' cambiado de '{old_val}' a '{new_val}'")
            if changes:
                QuoteHistory.objects.create(
                    quote=obj,
                    user=request.user,
                    action="; ".join(changes)
                )
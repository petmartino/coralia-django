from django.contrib import admin, messages
# --- DELETED --- Program and ProgramItem imports removed.
from .models import Quote, EventType, Package, QuoteHistory
from .views import generate_tracking_code

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active', 'order')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

# --- DELETED --- ProgramItemInline and ProgramAdmin have been completely removed.

class QuoteHistoryInline(admin.TabularInline):
    model = QuoteHistory
    extra = 0
    readonly_fields = ('user', 'timestamp', 'action')
    can_delete = False
    def has_add_permission(self, request, obj=None): return False

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost')
    list_filter = ('status', 'event_type', 'event_date', 'created_by_source')
    # --- UPDATED --- Removed program__name from search
    search_fields = ('tracking_code', 'client_name', 'client_email', 'event_address')
    readonly_fields = ('tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user', 'total_cost', 'calculation_log')
    inlines = [QuoteHistoryInline]

    fieldsets = (
        # --- UPDATED --- Removed 'program' field from this fieldset
        ('Información General', { 'fields': ('tracking_code', 'client_name', 'status', 'event_type', 'package') }),
        ('Detalles del Evento', { 'fields': ('event_date', 'event_time', 'location_type', 'event_address', 'is_exterior', 'dress_code') }),
        ('Agrupación (si no se usa paquete)', { 'fields': ('num_voices', 'num_musicians') }),
        ('Pago y Costo', { 'fields': ('paid_amount', 'discount', 'total_cost') }),
        ('Contacto del Cliente', { 'fields': ('client_email', 'client_phone', 'contact_method', 'comments') }),
    )

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing
        if not obj.tracking_code: obj.tracking_code = generate_tracking_code()
        
        # Pass the instance directly to the pricing function
        pricing_breakdown, log = calculate_pricing(obj)

        for key, value in pricing_breakdown.items(): setattr(obj, key, value)
        obj.calculation_log = log

        if not obj.pk: obj.created_by_source = 'ADMIN'
        obj.created_by_user = request.user
        super().save_model(request, obj, form, change)
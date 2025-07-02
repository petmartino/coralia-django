from django.contrib import admin
from django.utils.html import mark_safe
# I see `generate_tracking_code` is imported, but we need the other util function
from .models import Quote, EventType, Package, QuoteHistory
from .views import generate_tracking_code 

# ... PackageAdmin, EventTypeAdmin, and QuoteHistoryInline classes are correct ...
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active', 'order')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_funeral_type', 'has_wedding_fee')
    list_editable = ('order',)

class QuoteHistoryInline(admin.TabularInline):
    model = QuoteHistory
    extra = 0
    readonly_fields = ('user', 'timestamp', 'action')
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost_display')
    list_filter = ('status', 'event_type', 'event_date', 'created_by_source')
    search_fields = ('tracking_code', 'client_name', 'client_email', 'event_address')
    readonly_fields = (
        'tracking_code', 'created_at', 'updated_at', 
        'display_details_and_log',
        'total_cost_display', 'payment_per_musician', 'outstanding_balance_display'
    )
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('tracking_code', 'client_name', 'status', 'event_type')
        }),
        ('Detalles del Evento y Agrupación', {
            'fields': ('package', ('event_date', 'event_time'), ('location_type', 'is_exterior'), 'event_address', 'dress_code', ('num_voices', 'num_musicians'))
        }),
        ('Detalles del Cliente', {
            'fields': ('client_phone', 'client_email', 'contact_method', 'comments')
        }),
        ('Costo y Pago', {
            'fields': (
                'discount', 'extra_charge', 'paid_amount', 
                'payment_per_musician', 'total_cost_display', 'outstanding_balance_display'
            )
        }),
        ('Cálculos y Registros (Automático)', {
            'classes': ('collapse',), 
            'fields': ('display_details_and_log', 'created_by_source', 'created_by_user'),
        }),
    )

    inlines = [QuoteHistoryInline]
    
    @admin.display(description='Costo Total')
    def total_cost_display(self, obj):
        return f"${obj.total_cost:,.2f}"

    @admin.display(description='Saldo Pendiente')
    def outstanding_balance_display(self, obj):
        return f"${obj.outstanding_balance:,.2f}"

    @admin.display(description="Detalles de Cálculo y Registro")
    def display_details_and_log(self, obj):
        style = "font-family: monospace; white-space: pre-wrap; background-color: #2d2d2d; color: #f0f0f0; padding: 10px; border: 1px solid #444; border-radius: 4px;"
        
        extra_charge_html = ""
        if obj.extra_charge != 0:
            extra_charge_html = f"<li><strong>Cargo Extra / Ajuste:</strong> ${obj.extra_charge:,.2f}</li>"

        html = f"""
        <details>
            <summary style="cursor: pointer;"><strong>Ver/Ocultar Desglose y Registro de Cálculo</strong></summary>
            <div style="padding-top: 10px;">
                <h4>Desglose de Costos</h4>
                <ul>
                    <li><strong>Costo Base Músicos:</strong> ${obj.cost_musicians_base:,.2f}</li>
                    <li><strong>Aumento Vestimenta:</strong> ${obj.cost_gala_fee:,.2f}</li>
                    <li><strong>Aumento Horario Estelar:</strong> ${obj.cost_primetime_fee:,.2f}</li>
                    <li><strong>Aumento Distancia:</strong> ${obj.cost_distance_fee:,.2f}</li>
                    <li><strong>Gestión (Base):</strong> ${obj.cost_manager_base:,.2f}</li>
                    <li><strong>Gestión (Por Músico):</strong> ${obj.cost_manager_per_person:,.2f}</li>
                    <li><strong>Gestión (Exterior):</strong> ${obj.cost_manager_exterior:,.2f}</li>
                    <li><strong>Gestión (Boda):</strong> ${obj.cost_manager_boda:,.2f}</li>
                    <li><strong>Transporte:</strong> ${obj.cost_car_fee:,.2f}</li>
                    {extra_charge_html}
                </ul>
                <h4>Registro de Cálculo</h4>
                <pre style="{style}">{obj.calculation_log}</pre>
            </div>
        </details>
        """
        return mark_safe(html)

    def save_model(self, request, obj, form, change):
        # --- FIX: ADD THIS IMPORT ---
        from .utils import calculate_pricing

        is_new = not obj.pk
        
        original_status = None
        if not is_new:
            original_status = Quote.objects.get(pk=obj.pk).status

        if not obj.tracking_code:
            obj.tracking_code = generate_tracking_code()
        
        # This line will now work because of the import above
        pricing_breakdown, log = calculate_pricing(obj)
        for key, value in pricing_breakdown.items():
            setattr(obj, key, value)
        obj.calculation_log = log

        if is_new:
            obj.created_by_source = 'ADMIN'
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)
        
        if is_new:
            QuoteHistory.objects.create(quote=obj, user=request.user, action="Cotización creada en el panel de Admin.")
        
        if not is_new and original_status != obj.status:
            original_status_display = Quote.QuoteStatus(original_status).label
            new_status_display = obj.get_status_display()
            action_text = f"Estado cambiado de '{original_status_display}' a '{new_status_display}'."
            QuoteHistory.objects.create(quote=obj, user=request.user, action=action_text)
from django.contrib import admin
from django.utils.html import mark_safe
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
    readonly_fields = ('tracking_code', 'created_at', 'updated_at', 'display_details_and_log')
    
    # Organize fields into logical groups (fieldsets)
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
            'fields': ('discount', 'paid_amount')
        }),
        ('Cálculos y Registros (Automático)', {
            'classes': ('collapse',), # This fieldset will be collapsible
            'fields': ('display_details_and_log', 'created_by_source', 'created_by_user'),
        }),
    )

    inlines = [QuoteHistoryInline]
    
    @admin.display(description='Costo Total')
    def total_cost_display(self, obj):
        return f"${obj.total_cost:,.2f}"

    @admin.display(description="Detalles de Cálculo y Registro")
    def display_details_and_log(self, obj):
        # Using the <details> and <summary> tags for a native, JS-free accordion
        html = f"""
        <details>
            <summary><strong>Ver/Ocultar Desglose y Registro de Cálculo</strong></summary>
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
                <li><strong>Pago por Músico (redondeado):</strong> ${obj.payment_per_musician:,.2f}</li>
            </ul>
            <h4>Registro de Cálculo</h4>
            <pre style="font-family: monospace; white-space: pre-wrap; background: #f4f4f4; padding: 10px; border-radius: 4px;">{obj.calculation_log}</pre>
        </details>
        """
        return mark_safe(html)

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing
        
        # Track original status if the object is being changed
        original_obj = None
        if change:
            original_obj = Quote.objects.get(pk=obj.pk)

        if not obj.tracking_code:
            obj.tracking_code = generate_tracking_code()
            QuoteHistory.objects.create(quote=obj, user=request.user, action="Cotización creada.")

        pricing_breakdown, log = calculate_pricing(obj)

        for key, value in pricing_breakdown.items():
            setattr(obj, key, value)
        obj.calculation_log = log

        if not obj.pk:
            obj.created_by_source = 'ADMIN'
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)
        
        # Create history entry if status changed
        if change and original_obj and original_obj.status != obj.status:
            action_text = f"Estado cambiado de '{original_obj.get_status_display()}' a '{obj.get_status_display()}'."
            QuoteHistory.objects.create(quote=obj, user=request.user, action=action_text)
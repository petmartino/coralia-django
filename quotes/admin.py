from django.contrib import admin, messages
from django import forms
from django.utils.html import mark_safe
from .models import Quote, EventType, Package
from programs.models import Program, ProgramItem
from .views import generate_tracking_code
from programs.admin import ProgramInline

class QuoteAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --- UI FIX: REMOVE ALL EXTRA LINKS FROM DROPDOWNS ---
        for field_name in ['program_template', 'package', 'event_type']:
            if field_name in self.fields:
                widget = self.fields[field_name].widget
                widget.can_add_related = False
                widget.can_change_related = False
                widget.can_delete_related = False
                widget.can_view_related = False

    class Meta:
        model = Quote
        fields = '__all__'
        widgets = { 'event_address': forms.Textarea(attrs={'rows': 3}), }

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_singers', 'num_instrument_players', 'is_active', 'order')
    list_editable = ('is_active', 'order')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_funeral_type', 'has_wedding_fee')
    list_editable = ('order',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    form = QuoteAdminForm
    inlines = [ProgramInline]
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date')
    list_filter = ('status', 'event_type', 'event_date')
    search_fields = ('tracking_code', 'client_name', 'event_address')
    readonly_fields = ('tracking_code', 'created_at', 'updated_at', 'display_calculation_log', 'total_cost_display', 'outstanding_balance_display', 'payment_per_musician')
    
    fieldsets = (
        ('Información Principal', {'fields': ('tracking_code', 'client_name', 'status', 'event_type')}),
        ('Detalles del Evento', {'fields': ('package', ('event_date', 'event_time'), 'location_type', 'event_address', 'dress_code', ('num_voices', 'num_musicians'))}),
        ('Aplicar Plantilla de Programa', {'description': '<b>Advertencia:</b> Al seleccionar una plantilla y guardar, se <b>creará o sobrescribirá por completo</b> el programa de esta cotización.','fields': ('program_template',)}),
        ('Costo y Pago', {'fields': ('total_cost_display', 'discount', 'extra_charge', 'paid_amount', 'outstanding_balance_display')}),
        ('Cálculos Detallados (Solo Lectura)', {'classes': ('collapse',), 'fields': ('display_calculation_log',)})
    )
        
    @admin.display(description='Costo Total')
    def total_cost_display(self, obj):
        return f"${obj.total_cost:,.2f}"

    @admin.display(description='Saldo Pendiente')
    def outstanding_balance_display(self, obj):
        return f"${obj.outstanding_balance:,.2f}"

    @admin.display(description="Registro de Cálculo")
    def display_calculation_log(self, obj):
        # --- UI FIX: GRAY BACKGROUND WITH WHITE TEXT ---
        style = "font-family: monospace; white-space: pre-wrap; background-color: #4a4a4a; color: #fff; padding: 10px; border-radius: 4px;"
        return mark_safe(f'<pre style="{style}">{obj.calculation_log or "No hay registro."}</pre>')

    def get_inline_instances(self, request, obj=None):
        if not obj: # Don't show Program box for new, unsaved Quotes
            return []
        return super().get_inline_instances(request, obj)
    
    def get_form(self, request, obj=None, **kwargs):
        # This makes sure our custom form is always used.
        kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing

        is_new = not obj.pk
        if is_new and not obj.tracking_code:
            obj.tracking_code = generate_tracking_code()

        super().save_model(request, obj, form, change) # Save Quote first

        program_template = form.cleaned_data.get('program_template')
        if program_template:
            # --- FEATURE: Overwrite/Create Program from Template ---
            program, created = Program.objects.get_or_create(quote=obj)
            
            # Safely get a name for the program
            event_name = obj.event_type.name if obj.event_type else 'Evento'
            program.name = f"Programa para {event_name} - {obj.client_name}"
            
            if not created:
                program.items.all().delete()
                messages.warning(request, 'El programa existente fue sobrescrito con la nueva plantilla.')
            else:
                messages.success(request, 'Se creó un programa a partir de la plantilla seleccionada.')

            for item in program_template.items.order_by('order'):
                ProgramItem.objects.create(program=program, piece=item.piece, order=item.order)
            program.save()
            obj.program_template = None

        pricing, log = calculate_pricing(obj)
        for key, value in pricing.items():
            setattr(obj, key, value)
        obj.calculation_log = log
        super().save_model(request, obj, form, change)

    # --- THE DEFINITIVE FIX FOR THE DELETION ERROR ---
    def delete_queryset(self, request, queryset):
        for quote in queryset:
            if hasattr(quote, 'program'):
                quote.program.delete()
        super().delete_queryset(request, queryset)

    def delete_model(self, request, obj):
        if hasattr(obj, 'program'):
            obj.program.delete()
        super().delete_model(request, obj)
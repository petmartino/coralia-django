# quotes/admin.py (Final Correct Version)

from django.contrib import admin
from .models import Quote, Program, ProgramItem
from main.models import RepertoirePiece
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# This class MUST inherit from admin.TabularInline to get the side-handle layout.
class ProgramItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProgramItem
    extra = 1
    # We define the fields to show them as columns in the table.
    fields = ('repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']

@admin.register(Program)
# This class MUST inherit from SortableAdminMixin to enable the inline's JS.
class ProgramAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProgramItemInline]
    
    # By defining list_display WITHOUT the special 'my_order' field, we prevent
    # the main list from being sortable, even though the mixin is active.
    list_display = ('__str__', 'quote_tracking_code', 'piece_count')
    search_fields = ['name', 'quote__tracking_code']

    @admin.display(description='Quote ID')
    def quote_tracking_code(self, obj):
        if hasattr(obj, 'quote'):
            return obj.quote.tracking_code
        return "N/A"
    
    @admin.display(description='Nº Piezas')
    def piece_count(self, obj):
        return obj.items.count()

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'client_name', 'event_type', 'event_date', 'total_cost', 'created_at')
    list_filter = ('event_type', 'event_date', 'created_at')
    search_fields = ('tracking_code', 'client_name', 'client_email')
    readonly_fields = ('tracking_code', 'created_at', 'updated_at')
    fieldsets = (
        ('Información General', {
            'fields': ('tracking_code', 'client_name', 'event_type', 'program')
        }),
        ('Detalles del Evento', {
            'fields': ('event_date', 'event_time', 'location_type', 'is_exterior', 'dress_code'),
        }),
        ('Contacto del Cliente', {
            'fields': ('client_email', 'client_phone', 'contact_method')
        }),
        ('Agrupación', {
            'fields': ('num_voices', 'num_musicians')
        }),
        ('Costos y Comentarios', {
            'classes': ('collapse',),
            'fields': ('comments', 'total_cost', 'cost_musicians_base', 'total_musician_payout_rounded'),
        }),
    )
# quotes/admin.py

from django.contrib import admin
from .models import Quote, Program, ProgramItem, EventType
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# --- NEW ADMIN CLASS FOR EVENT TYPES ---
@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


class ProgramItemInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProgramItem
    extra = 1
    fields = ('repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']


@admin.register(Program)
class ProgramAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProgramItemInline]
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
    # --- UPDATED list_display, list_filter, search_fields and readonly_fields ---
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost', 'created_at', 'created_by_source')
    list_filter = ('status', 'event_type', 'event_date', 'created_at', 'created_by_source')
    search_fields = ('tracking_code', 'client_name', 'client_email')
    readonly_fields = ('tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user')
    
    fieldsets = (
        ('Información General', {
            'fields': ('tracking_code', 'client_name', 'event_type', 'program', 'status')
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
        ('Información de Creación', {
            'classes': ('collapse',),
            'fields': ('created_by_source', 'created_by_user', 'created_at', 'updated_at')
        }),
        ('Costos y Comentarios', {
            'classes': ('collapse',),
            'fields': ('comments', 'total_cost', 'cost_musicians_base', 'total_musician_payout_rounded'),
        }),
    )

    # --- NEW METHOD to automatically set the user ---
    def save_model(self, request, obj, form, change):
        # When a quote is saved in the admin, set the source to ADMIN and the user to the current user
        if not obj.pk: # If creating a new quote
            obj.created_by_source = Quote.CreatedSource.ADMIN
        
        # Always update the user who last saved it
        obj.created_by_user = request.user
        
        super().save_model(request, obj, form, change)
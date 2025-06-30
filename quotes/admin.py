# quotes/admin.py

from django.contrib import admin, messages
from .models import Quote, Program, ProgramItem, EventType, Package, QuoteHistory
from .views import generate_tracking_code

# Completely removed all ties to adminsortable2 for programs

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

class ProgramItemInline(admin.TabularInline):
    model = ProgramItem
    extra = 1
    fields = ('order', 'repertoire_piece',)
    autocomplete_fields = ['repertoire_piece']
    ordering = ('order',)

@admin.action(description='Clonar programas seleccionados')
def clone_programs(modeladmin, request, queryset):
    for program in queryset:
        original_pk = program.pk
        original_items = list(ProgramItem.objects.filter(program_id=original_pk))
        program.pk = None
        program.name = f"Copia de {program.name}"
        program.save()
        items_to_clone = [ProgramItem(program=program, repertoire_piece=item.repertoire_piece, order=item.order) for item in original_items]
        ProgramItem.objects.bulk_create(items_to_clone)
    modeladmin.message_user(request, f"{queryset.count()} programas han sido clonados.", messages.SUCCESS)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'piece_count')
    list_editable = ('order',)  # 'name' is the link by default
    list_display_links = ('name',) # Explicitly make name the link
    search_fields = ['name']
    inlines = [ProgramItemInline]
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

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'client_name', 'event_type', 'status', 'event_date', 'total_cost')
    list_filter = ('status', 'event_type', 'event_date')
    search_fields = ('tracking_code', 'client_name', 'program__name')
    readonly_fields = ('tracking_code', 'created_at', 'updated_at', 'created_by_source', 'created_by_user', 'total_cost', 'calculation_log')
    inlines = [QuoteHistoryInline]

    def save_model(self, request, obj, form, change):
        from .utils import calculate_pricing
        if not obj.tracking_code: obj.tracking_code = generate_tracking_code()
        pricing_breakdown, log = calculate_pricing(form.cleaned_data)
        for key, value in pricing_breakdown.items(): setattr(obj, key, value)
        obj.calculation_log = log
        if not obj.pk: obj.created_by_source = 'ADMIN'
        obj.created_by_user = request.user
        super().save_model(request, obj, form, change)
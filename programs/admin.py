from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from django import forms
from django.utils.html import format_html, mark_safe

from .models import Program, ProgramItem

class ProgramAdminForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = { 'notes': forms.Textarea(attrs={'rows': 3}), }

class ProgramItemInline(admin.TabularInline):
    model = ProgramItem
    extra = 1
    autocomplete_fields = ['piece']
    fields = ('order', 'piece')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    form = ProgramAdminForm
    inlines = [ProgramItemInline]
    fieldsets = ((None, {'fields': ('name', 'notes')}),)
    
    # Hide from main admin index
    def get_model_perms(self, request):
        return {}
    
    # --- UI/UX FIX: HIDE UNWANTED BUTTONS ---
    # Hide "Save and add another"
    save_as_continue = False

    def has_delete_permission(self, request, obj=None):
        return False # Hide "Delete" button from this page

    # --- UI/UX FIX: ALWAYS REDIRECT BACK TO THE QUOTE ON SAVE ---
    def response_change(self, request, obj):
        # Always redirect to the quote page after saving.
        quote_url = reverse('admin:quotes_quote_change', args=[obj.quote.pk])
        return redirect(quote_url)

class ProgramInline(admin.StackedInline):
    model = Program
    fields = ('display_program_summary',)
    readonly_fields = ('display_program_summary',)
    can_delete = True
    max_num = 0

    @admin.display(description='Programa Actual')
    def display_program_summary(self, obj):
        if not obj or not obj.pk:
            return "No existe un programa. Puede crear uno guardando esta cotización y luego haciendo clic en el enlace que aparecerá."
            
        link = reverse('admin:programs_program_change', args=[obj.pk])
        edit_link = f'<p><a href="{link}" class="button">Editar Programa</a></p>'

        # --- UI FIX: DISPLAY PROGRAM AS REQUESTED ---
        program_name = f"<h4 style='margin-bottom: 0.5em; font-weight: bold;'>{obj.name}</h4>"
        items = obj.items.order_by('order')

        if not items.exists():
            summary = "<p><em>Este programa está vacío.</em></p>"
        else:
            # Display list of pieces without order number, but with composer
            summary = "<ul style='margin-left: 0; padding-left: 0; list-style: none;'>"
            for item in items:
                composer = f" - <em>{item.piece.compositor}</em>" if item.piece and item.piece.compositor else ""
                piece_name = item.piece.nombre if item.piece else "Pieza no especificada"
                summary += f"<li>{piece_name}{composer}</li>"
            summary += "</ul>"
            
        return mark_safe(program_name + summary + edit_link)
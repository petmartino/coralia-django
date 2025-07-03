from django.contrib import admin
from django import forms
from .models import ProgramTemplate, ProgramTemplateItem

# A custom form to control the 'notes' widget size.
class ProgramTemplateAdminForm(forms.ModelForm):
    class Meta:
        model = ProgramTemplate
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

# This is a STANDARD Django inline, with no sorting library.
class ProgramTemplateItemInline(admin.TabularInline):
    model = ProgramTemplateItem
    extra = 1
    autocomplete_fields = ['piece']
    
    #
    # --- THIS IS THE CRITICAL UI FIX ---
    # We are now explicitly showing the 'order' field as a standard, editable number input.
    # The drag-and-drop handle is gone, but the input box will be visible and will work.
    #
    fields = ('order', 'piece')


# This is a STANDARD Django ModelAdmin, with no sorting library.
@admin.register(ProgramTemplate)
class ProgramTemplateAdmin(admin.ModelAdmin):
    # Use our form to get the right widget size.
    form = ProgramTemplateAdminForm
    
    # Use fieldsets to ensure the name and notes fields always appear.
    fieldsets = (
        (None, {
            'fields': ('name', 'notes')
        }),
    )

    list_display = ('name', 'item_count')
    search_fields = ('name',)
    
    # Include the now-standard inline.
    inlines = [ProgramTemplateItemInline]

    @admin.display(description='Nº de Piezas')
    def item_count(self, obj):
        return obj.items.count()
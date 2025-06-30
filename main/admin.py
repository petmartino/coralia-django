from django.contrib import admin
from .models import Tag, RepertoirePiece

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'piece_count', 'order')
    search_fields = ('name',)
    # UPDATED: Make 'order' editable
    list_editable = ('order',)

    @admin.display(description='Número de Piezas')
    def piece_count(self, obj):
        return obj.repertoire_pieces.count()

@admin.register(RepertoirePiece)
class RepertoirePieceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'compositor', 'display_tags')
    search_fields = ('nombre', 'compositor')
    list_filter = ('tags',)
    filter_horizontal = ('tags',) 

    @admin.display(description='Tags')
    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
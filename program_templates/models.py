from django.db import models
from main.models import RepertoirePiece

class ProgramTemplate(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nombre de la Plantilla")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas Internas")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Plantilla de Programa"
        verbose_name_plural = "Plantillas de Programas"
        ordering = ['name']

class ProgramTemplateItem(models.Model):
    template = models.ForeignKey(ProgramTemplate, related_name='items', on_delete=models.CASCADE)
    
    # This field MUST allow blank, because an empty 'extra' form row will be submitted.
    piece = models.ForeignKey(RepertoirePiece, on_delete=models.CASCADE, verbose_name="Pieza", blank=True, null=True)
    
    order = models.PositiveIntegerField(default=0)

    #
    # --- THIS IS THE FINAL, CORRECT __str__ FIX ---
    # It handles all states:
    # 1. In-memory object with no pk or piece yet.
    # 2. Saved object that might have a piece.
    # This method is guaranteed to return a string.
    #
    def __str__(self):
        if self.pk:
            return f"Pieza del programa (ID: {self.pk})"
        return "Nuevo elemento de programa"

    class Meta:
        ordering = ['order']
        verbose_name = "Pieza de Plantilla"
        verbose_name_plural = "Piezas de la Plantilla"
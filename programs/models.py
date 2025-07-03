from django.db import models
from main.models import RepertoirePiece

class Program(models.Model):
    quote = models.OneToOneField('quotes.Quote', on_delete=models.CASCADE, related_name="program")
    name = models.CharField(max_length=200, verbose_name="Nombre del Programa del Evento")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas del Programa")

    def __str__(self):
        return self.name or f"Programa para {self.quote.tracking_code}"

    # --- THIS IS THE FIX ---
    # We must add a Meta class and define a default ordering.
    # Ordering by name is a sensible default.
    class Meta:
        ordering = ['name']
        verbose_name = "Programa de Evento"
        verbose_name_plural = "Programas de Eventos"
    # -----------------------

class ProgramItem(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="items")
    # This piece field can be blank in the admin form before saving
    piece = models.ForeignKey(RepertoirePiece, on_delete=models.CASCADE, verbose_name="Pieza", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        if hasattr(self, 'piece') and self.piece:
            return f"Pieza: {self.piece.nombre}"
        return "Nueva Pieza (seleccionar y guardar)"

    class Meta:
        ordering = ['order']
        verbose_name = "Pieza del Programa"
        verbose_name_plural = "Piezas del Programa"
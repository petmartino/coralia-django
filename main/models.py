from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class RepertoirePiece(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre de la pieza musical.")
    compositor = models.CharField(max_length=150, blank=True, null=True, help_text="Compositor de la obra.")
    tonalidad = models.CharField(max_length=50, blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    letra_original = models.TextField(blank=True, null=True)
    letra_traducida = models.TextField(blank=True, null=True, help_text="Traducción al español, si aplica.")
    video_url = models.CharField(max_length=255, blank=True, null=True, help_text="URL de 'embed' de YouTube (ej. https://www.youtube.com/embed/VIDEO_ID)")
    tags = models.ManyToManyField(Tag, blank=True, related_name="repertoire_pieces")

    def __str__(self):
        return f"{self.nombre} ({self.compositor or 'N/A'})"

    def get_absolute_url(self):
        return reverse('main:repertorio_detail', args=[self.id])
    
    class Meta:
        verbose_name = "Pieza de Repertorio"
        verbose_name_plural = "Piezas de Repertorio"
        ordering = ['nombre']
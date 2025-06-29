# quotes/models.py

from django.db import models
from main.models import RepertoirePiece
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# New model for Event Types
class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, help_text="Order in which to display event types.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, default="Programa de Evento")
    pieces = models.ManyToManyField(RepertoirePiece, through='ProgramItem', related_name='programs')

    def __str__(self):
        quote_tracking = self.quote.tracking_code if hasattr(self, 'quote') else "N/A"
        return self.name or f"Programa para {quote_tracking}"

    class Meta:
        ordering = ['name']


class ProgramItem(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="items")
    repertoire_piece = models.ForeignKey(RepertoirePiece, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        if self.repertoire_piece:
            return self.repertoire_piece.nombre
        return "Empty Slot"


class Quote(models.Model):
    class QuoteStatus(models.TextChoices):
        UNCONFIRMED = 'UNCONFIRMED', _('Unconfirmed')
        CONFIRMED = 'CONFIRMED', _('Confirmed')
        COMPLETED = 'COMPLETED', _('Completed')
        CANCELLED = 'CANCELLED', _('Cancelled')
        EXPIRED = 'EXPIRED', _('Expired')

    class CreatedSource(models.TextChoices):
        WEBSITE = 'WEBSITE', _('Website')
        ADMIN = 'ADMIN', _('Admin')

    tracking_code = models.CharField(max_length=12, unique=True, db_index=True)
    
    # This is the final, correct field.
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Event Type"))
    
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    location_type = models.CharField(max_length=100, blank=True, null=True)
    location_details = models.CharField(max_length=300, blank=True, null=True)
    is_exterior = models.BooleanField(default=False)
    num_voices = models.IntegerField(default=1)
    num_musicians = models.IntegerField(default=1)
    dress_code = models.CharField(max_length=50, blank=True, null=True)
    client_name = models.CharField(max_length=150, blank=True, null=True)
    client_phone = models.CharField(max_length=50, blank=True, null=True)
    client_email = models.EmailField(max_length=150, blank=True, null=True)
    contact_method = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cost_musicians_base = models.FloatField(default=0)
    cost_weekend_fee = models.FloatField(default=0)
    cost_distance_fee = models.FloatField(default=0)
    cost_gala_fee = models.FloatField(default=0)
    cost_primetime_fee = models.FloatField(default=0)
    cost_manager_base = models.FloatField(default=0)
    cost_manager_per_person = models.FloatField(default=0)
    cost_manager_exterior = models.FloatField(default=0)
    cost_manager_boda = models.FloatField(default=0)
    cost_car_fee = models.FloatField(default=0)
    total_musician_payout_rounded = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    
    # These are the correct new fields.
    status = models.CharField(max_length=20, choices=QuoteStatus.choices, default=QuoteStatus.UNCONFIRMED, db_index=True)
    created_by_source = models.CharField(max_length=20, choices=CreatedSource.choices, default=CreatedSource.WEBSITE)
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who created or last saved the quote in the admin.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    program = models.OneToOneField(Program, on_delete=models.SET_NULL, blank=True, null=True, related_name='quote')

    def __str__(self):
        return f"Cotización {self.tracking_code} para {self.client_name}"

    class Meta:
        ordering = ['-created_at']
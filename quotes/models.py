# quotes/models.py

from django.db import models
from main.models import RepertoirePiece
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import math

# NEW: Model for pre-defined packages
class Package(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    num_singers = models.PositiveIntegerField(default=1, verbose_name="Número de Voces")
    num_instrument_players = models.PositiveIntegerField(default=1, verbose_name="Número de Músicos")
    is_active = models.BooleanField(default=True, help_text="Show this package as an option in the quote form.")

    def __str__(self):
        return f"{self.name} ({self.num_singers} voces, {self.num_instrument_players} músicos)"
    
    class Meta:
        ordering = ['name']


# UPDATED: EventType model with pricing rules
class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, help_text="Order in which to display event types.")
    
    # NEW Pricing rule fields
    is_funeral_type = models.BooleanField(default=False, help_text="Does this event type (e.g., funeral) always use the weekday musician rate?")
    has_wedding_fee = models.BooleanField(default=False, help_text="Does this event type have the special wedding manager fee?")
    manager_base_fee = models.FloatField(default=200.0, help_text="The base fee for the manager for this type of event.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

# Add an order field to Program, but don't use adminsortable2 for it
class Program(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, default="Programa de Evento")
    pieces = models.ManyToManyField(RepertoirePiece, through='ProgramItem', related_name='programs')
    # NEW: Simple ordering field to break the dependency on adminsortable2's problematic magic
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        # Make the __str__ more robust for when quote is not yet linked
        if hasattr(self, 'quote') and self.quote:
            return self.name or f"Programa para {self.quote.tracking_code}"
        return self.name or f"Programa sin cotización asignada"

    class Meta:
        # THIS IS THE CRITICAL FIX for the ValueError.
        # It tells the admin to use the integer 'order' field for sorting.
        ordering = ['order']


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

    LOCATION_CHOICES = [
        ('dentro_periferico', 'Dentro del periférico de Guadalajara'),
        ('fuera_periferico', 'Fuera del periférico (ZMG)'),
        ('1_hora', 'A 1 hora de Guadalajara'),
        ('2_horas', 'A 2 horas de Guadalajara'),
        ('3_horas', 'A más de 3 horas de Guadalajara'),
    ]
    DRESS_CODE_CHOICES = [('Formal-Casual', 'Formal-Casual'), ('Formal', 'Formal'), ('Gala', 'Gala')]

    tracking_code = models.CharField(max_length=12, unique=True, db_index=True)
    
    # Relationships
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Event Type"))
    program = models.OneToOneField(Program, on_delete=models.SET_NULL, blank=True, null=True, related_name='quote')
    # NEW: Link to a package, can be null
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Paquete Seleccionado")
    
    # Event Details
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    location_type = models.CharField(max_length=100, blank=True, null=True, choices=LOCATION_CHOICES, verbose_name="Ubicación")
    # NEW: event address field
    event_address = models.CharField(max_length=512, blank=True, null=True, verbose_name="Dirección del Evento")
    is_exterior = models.BooleanField(default=False)
    
    # Ensemble Details (used if no package is selected)
    num_voices = models.IntegerField(default=1)
    num_musicians = models.IntegerField(default=1)
    dress_code = models.CharField(max_length=50, blank=True, null=True, choices=DRESS_CODE_CHOICES, verbose_name="Código de Vestimenta")

    # Client Details
    client_name = models.CharField(max_length=150, blank=True, null=True)
    client_phone = models.CharField(max_length=50, blank=True, null=True)
    client_email = models.EmailField(max_length=150, blank=True, null=True)
    contact_method = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # Cost Breakdown (auto-calculated)
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
    # NEW: System-calculated payment per musician
    payment_per_musician = models.FloatField(default=0, help_text="Pago individual por músico, calculado por el sistema.")

    # Pricing & Payment
    # NEW: discount and paid amount fields
    discount = models.FloatField(default=0, verbose_name="Descuento (cantidad fija)")
    paid_amount = models.FloatField(default=0, verbose_name="Monto Pagado")
    total_cost = models.FloatField(default=0)
    
    # Meta
    status = models.CharField(max_length=20, choices=QuoteStatus.choices, default=QuoteStatus.UNCONFIRMED, db_index=True)
    created_by_source = models.CharField(max_length=20, choices=CreatedSource.choices, default=CreatedSource.WEBSITE)
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who created or last saved the quote in the admin.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cotización {self.tracking_code} para {self.client_name}"

    def recalculate_total_cost(self, save=True):
        """ Recalculates all costs based on the quote's current fields. """
        # This logic will be very similar to the one in your view,
        # we will centralize it here later. For now, this is a placeholder.
        # The actual logic will be implemented in Stage 2 (save_model)
        # to avoid repeating it. For now, let's just update the total.
        
        cost_sum = sum([
            self.cost_musicians_base, self.cost_weekend_fee,
            self.cost_distance_fee, self.cost_gala_fee, self.cost_primetime_fee,
            self.cost_manager_base, self.cost_manager_per_person,
            self.cost_manager_exterior, self.cost_manager_boda, self.cost_car_fee
        ])
        
        self.total_cost = cost_sum - self.discount

        if save:
            self.save(update_fields=['total_cost'])
            
    @property
    def total_people(self):
        if self.package:
            return self.package.num_singers + self.package.num_instrument_players
        return self.num_voices + self.num_musicians

    class Meta:
        ordering = ['-created_at']

# NEW: Simple history tracking
class QuoteHistory(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255, help_text="Describes the change, e.g., 'Status changed from Confirmed to Completed'.")

    def __str__(self):
        return f"History for {self.quote.tracking_code} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
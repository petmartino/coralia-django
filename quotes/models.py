# quotes/models.py
from django.db import models
from main.models import RepertoirePiece
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import math

class Package(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    num_singers = models.PositiveIntegerField(default=1, verbose_name="Número de Voces")
    num_instrument_players = models.PositiveIntegerField(default=1, verbose_name="Número de Músicos")
    is_active = models.BooleanField(default=True, help_text="Show this package as an option in the quote form.")
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display packages on the website.")
    def __str__(self): return f"{self.name} ({self.num_singers}v, {self.num_instrument_players}m)"
    class Meta: ordering = ['order', 'name']

class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display event types.")
    is_funeral_type = models.BooleanField(default=False, help_text="Funerals always use weekday rates.")
    has_wedding_fee = models.BooleanField(default=False, help_text="Adds special manager fee for weddings.")
    manager_base_fee = models.FloatField(default=200.0, help_text="Base manager fee for this event.")
    def __str__(self): return self.name
    class Meta: ordering = ['order']

class Program(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, default="Programa de Evento")
    pieces = models.ManyToManyField(RepertoirePiece, through='ProgramItem', related_name='programs')
    order = models.PositiveIntegerField(default=0, help_text="Order in admin lists (lower numbers first).")
    def __str__(self): return self.name or "Programa sin nombre"
    class Meta: ordering = ['order', 'name']

# THIS IS THE CRUCIAL CHANGE
class ProgramItem(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="items")
    repertoire_piece = models.ForeignKey(RepertoirePiece, on_delete=models.CASCADE)
    # The field is now named 'order'
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        # We order by this new field.
        ordering = ['order']
    def __str__(self):
        return self.repertoire_piece.nombre if self.repertoire_piece else "Empty Slot"

# ... rest of the file (Quote, QuoteHistory) is correct.
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

    LOCATION_CHOICES = [('dentro_periferico', 'Dentro del periférico de Guadalajara'), ('fuera_periferico', 'Fuera del periférico (ZMG)'), ('1_hora', 'A 1 hora de Guadalajara'), ('2_horas', 'A 2 horas de Guadalajara'), ('3_horas', 'A más de 3 horas de Guadalajara')]
    DRESS_CODE_CHOICES = [('Formal-Casual', 'Formal-Casual'), ('Formal', 'Formal'), ('Gala', 'Gala')]
    CONTACT_METHOD_CHOICES = [('WhatsApp', 'WhatsApp'), ('Llamada Telefónica', 'Llamada Telefónica'), ('Correo Electrónico', 'Correo Electrónico')]

    tracking_code = models.CharField(max_length=12, unique=True, db_index=True, blank=True)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Event Type"))
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, blank=True, null=True, related_name='quotes')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Paquete Seleccionado")
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    location_type = models.CharField(max_length=100, blank=True, null=True, choices=LOCATION_CHOICES, verbose_name="Ubicación")
    event_address = models.CharField(max_length=512, blank=True, null=True, verbose_name="Dirección del Evento")
    is_exterior = models.BooleanField(default=False)
    num_voices = models.IntegerField(default=1)
    num_musicians = models.IntegerField(default=1)
    dress_code = models.CharField(max_length=50, blank=True, null=True, choices=DRESS_CODE_CHOICES, verbose_name="Código de Vestimenta")
    client_name = models.CharField(max_length=150, blank=True, null=True)
    client_phone = models.CharField(max_length=50, blank=True, null=True)
    client_email = models.EmailField(max_length=150, blank=True, null=True)
    contact_method = models.CharField(max_length=50, blank=True, null=True, choices=CONTACT_METHOD_CHOICES, verbose_name="Método de Contacto")
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
    payment_per_musician = models.FloatField(default=0, help_text="Pago individual por músico, calculado por el sistema.")
    discount = models.FloatField(default=0, verbose_name="Descuento (cantidad fija)")
    paid_amount = models.FloatField(default=0, verbose_name="Monto Pagado")
    total_cost = models.FloatField(default=0)
    calculation_log = models.TextField(blank=True, null=True, editable=False, verbose_name="Registro de Cálculo")
    status = models.CharField(max_length=20, choices=QuoteStatus.choices, default=QuoteStatus.UNCONFIRMED, db_index=True)
    created_by_source = models.CharField(max_length=20, choices=CreatedSource.choices, default=CreatedSource.WEBSITE)
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who created or last saved the quote in the admin.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return f"Cotización {self.tracking_code or '(sin código)'} para {self.client_name or 'cliente'}"
    @property
    def fifty_percent_deposit(self): return self.total_cost / 2 if self.total_cost else 0
    @property
    def total_people(self):
        if self.package: return self.package.num_singers + self.package.num_instrument_players
        return self.num_voices + self.num_musicians
    class Meta: ordering = ['-created_at']

class QuoteHistory(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255, help_text="Describes the change, e.g., 'Status changed from Confirmed to Completed'.")
    class Meta: ordering = ['-timestamp']
    def __str__(self): return f"History for {self.quote.tracking_code} at {self.timestamp}"
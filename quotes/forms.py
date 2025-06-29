# quotes/forms.py

from django import forms
from .models import EventType # <-- ADD THIS IMPORT

class QuoteForm(forms.Form):
    # Step 1 Fields
    LOCATION_CHOICES = [
        ('dentro_periferico', 'Dentro del periférico de Guadalajara'),
        ('fuera_periferico', 'Fuera del periférico (ZMG)'),
        ('1_hora', 'A 1 hora de Guadalajara'),
        ('2_horas', 'A 2 horas de Guadalajara'),
        ('3_horas', 'A más de 3 horas de Guadalajara'),
    ]
    
    # --- THIS FIELD IS NOW A MODELCHOICEFIELD ---
    event_type = forms.ModelChoiceField(
        queryset=EventType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tipo de Evento"
    )

    event_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    event_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}))
    location_type = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select())
    is_exterior = forms.BooleanField(required=False)
    
    # Step 2 Fields
    VOICE_CHOICES = [(i, f'{i} Voz' if i==1 else f'{i} Voces') for i in [1, 2, 3, 4, 8]]
    MUSICIAN_CHOICES = [(i, f'{i} Músico' if i==1 else f'{i} Músicos') for i in [1, 2, 3, 4, 6]]
    DRESS_CODE_CHOICES = [('Formal-Casual', 'Formal-Casual'), ('Formal', 'Formal'), ('Gala', 'Gala')]
    num_voices = forms.ChoiceField(choices=VOICE_CHOICES, widget=forms.Select())
    num_musicians = forms.ChoiceField(choices=MUSICIAN_CHOICES, widget=forms.Select())
    dress_code = forms.ChoiceField(choices=DRESS_CODE_CHOICES, widget=forms.Select())
    
    # Step 3 Fields
    CONTACT_METHOD_CHOICES = [('WhatsApp', 'WhatsApp'), ('Llamada Telefónica', 'Llamada Telefónica'), ('Correo Electrónico', 'Correo Electrónico')]
    client_name = forms.CharField(max_length=150, required=True)
    client_phone = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'pattern': '[0-9]{10}'}))
    client_email = forms.EmailField(max_length=150, required=False)
    contact_method = forms.ChoiceField(choices=CONTACT_METHOD_CHOICES, widget=forms.Select())
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('client_phone')
        email = cleaned_data.get('client_email')
        if not phone and not email:
            raise forms.ValidationError(
                "Debe proporcionar al menos un número de teléfono o un correo electrónico."
            )

class TrackerForm(forms.Form):
    tracking_code = forms.CharField(label="Ingresa su código de 8 dígitos:", max_length=12, required=True)
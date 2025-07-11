# quotes/views.py
import uuid
import base58
# --- ADD THESE IMPORTS ---
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
# -------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Quote, Package
from .forms import QuoteForm, TrackerForm
from .utils import calculate_pricing

def generate_tracking_code():
    while True:
        code = base58.b58encode(uuid.uuid4().bytes).decode('utf-8')[:8].lower()
        if not Quote.objects.filter(tracking_code=code).exists():
            return code

def cotizador_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pricing_breakdown, calculation_log_str = calculate_pricing(data)
            new_quote = Quote(
                tracking_code=generate_tracking_code(),
                event_date=data.get('event_date'),
                event_time=data.get('event_time'),
                event_type=data.get('event_type'),
                package=data.get('package'),
                location_type=data.get('location_type'),
                event_address=data.get('event_address'),
                is_exterior=data.get('is_exterior', False),
                num_voices=int(data.get('num_voices', 1)) if data.get('num_voices') else 0,
                num_musicians=int(data.get('num_musicians', 1)) if data.get('num_musicians') else 0,
                dress_code=data.get('dress_code'),
                client_name=data.get('client_name'),
                client_phone=data.get('client_phone'),
                client_email=data.get('client_email'),
                contact_method=data.get('contact_method'),
                comments=data.get('comments'),
                calculation_log=calculation_log_str,
                **pricing_breakdown 
            )
            new_quote.save()

            # --- ADD EMAIL SENDING LOGIC ---
            if new_quote.client_email:
                subject = f"Confirmación de Cotización Coralia: {new_quote.tracking_code}"
                context = {'quote': new_quote}
                html_message = render_to_string('emails/quote_confirmation.html', context)
                plain_message = render_to_string('emails/quote_confirmation.txt', context)
                
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [new_quote.client_email],
                    html_message=html_message,
                    fail_silently=False # Set to False during development to see errors
                )
            # --------------------------------

            return redirect(reverse('quotes:ver_cotizacion', args=[new_quote.tracking_code]))
    else:
        form = QuoteForm()
    tracker_form = TrackerForm()
    packages = Package.objects.filter(is_active=True).order_by('order')
    return render(request, 'quotes/cotizador.html', {'form': form, 'tracker_form': tracker_form, 'packages': packages})

def ver_cotizacion_view(request, code):
    code = code.lower()
    quote = get_object_or_404(Quote, tracking_code=code)
    return render(request, 'quotes/ver_cotizacion.html', {'quote': quote})

def cotizacion_detail_view(request, code):
    code = code.lower()
    quote = get_object_or_404(Quote.objects.select_related('package', 'event_type'), tracking_code=code)
    context = {
        'quote': quote,
        'show_payment_info': quote.status in ['CONFIRMED'],
    }
    return render(request, 'quotes/cotizacion_detail.html', context)

def rastrear_cotizacion_view(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('tracking_code').lower()
            quote = Quote.objects.filter(tracking_code=code).first()
            if quote:
                return redirect(reverse('quotes:cotizacion_detail', args=[code]))
    return redirect(reverse('quotes:cotizador'))
# quotes/views.py

import uuid
import base58
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Quote, Program, Package # Import Package
from .forms import QuoteForm, TrackerForm
from .utils import calculate_pricing # <-- Import our new function

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

            # --- 1. Calculate pricing using the centralized function ---
            pricing_breakdown = calculate_pricing(data)

            # --- 2. Create the Quote instance ---
            new_quote = Quote(
                tracking_code=generate_tracking_code(),
                event_date=data.get('event_date'),
                event_time=data.get('event_time'),
                event_type=data.get('event_type'),
                package=data.get('package'),
                location_type=data.get('location_type'),
                event_address=data.get('event_address'),
                is_exterior=data.get('is_exterior', False),
                num_voices=int(data.get('num_voices', 1)),
                num_musicians=int(data.get('num_musicians', 1)),
                dress_code=data.get('dress_code'),
                client_name=data.get('client_name'),
                client_phone=data.get('client_phone'),
                client_email=data.get('client_email'),
                contact_method=data.get('contact_method'),
                comments=data.get('comments'),
                **pricing_breakdown # Unpack all calculated values into the model
            )
            
            # --- If a program is needed, create an empty one ---
            if not new_quote.program:
                program = Program.objects.create(name=f"Programa para {new_quote.tracking_code}")
                new_quote.program = program

            new_quote.save()

            # --- 3. Send email (unchanged) ---
            if new_quote.client_email:
                email_context = {'quote': new_quote}
                html_message = render_to_string('emails/quote_confirmation.html', email_context)
                plain_message = render_to_string('emails/quote_confirmation.txt', email_context)
                send_mail(
                    subject=f'Confirmación de Cotización Coralia: #{new_quote.tracking_code}',
                    message=plain_message,
                    from_email=None,
                    recipient_list=['pedromartinezdelpaso@gmail.com'], # Or settings.EMAIL_HOST_USER
                    html_message=html_message,
                )

            # Redirect to the summary/preview page
            return redirect(reverse('quotes:ver_cotizacion', args=[new_quote.tracking_code]))
    else:
        form = QuoteForm()

    tracker_form = TrackerForm()
    # Also pass available packages to the template
    packages = Package.objects.filter(is_active=True)
    return render(request, 'quotes/cotizador.html', {'form': form, 'tracker_form': tracker_form, 'packages': packages})


def ver_cotizacion_view(request, code):
    """
    This is the simple confirmation/preview page shown immediately after creating a quote.
    """
    code = code.lower()
    quote = get_object_or_404(Quote, tracking_code=code)
    return render(request, 'quotes/ver_cotizacion.html', {'quote': quote})


# NEW VIEW for the full detail page
def cotizacion_detail_view(request, code):
    """
    This is the full detail page for a tracked quote, showing program, payment info etc.
    It can be the same as ver_cotizacion or a different template. Let's make a new one.
    """
    code = code.lower()
    quote = get_object_or_404(Quote.objects.select_related('program'), tracking_code=code)
    # Add payment details or contract info to context if needed
    context = {
        'quote': quote,
        'program_items': quote.program.items.select_related('repertoire_piece').all() if quote.program else [],
        'show_payment_info': quote.status == 'CONFIRMED', # Example logic
    }
    return render(request, 'quotes/cotizacion_detail.html', context)


def rastrear_cotizacion_view(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('tracking_code').lower()
            quote = Quote.objects.filter(tracking_code=code).first()
            if quote:
                # Redirect to the NEW detail view after tracking
                return redirect(reverse('quotes:cotizacion_detail', args=[code]))

    # If tracking fails, redirect back to the cotizador page
    # You might want to add a message here using Django's messaging framework
    return redirect(reverse('quotes:cotizador'))
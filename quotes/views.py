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

            # --- 1. Calculate pricing and get the log ---
            pricing_breakdown, calculation_log_str = calculate_pricing(data)

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
                num_voices=int(data.get('num_voices', 1)) if data.get('num_voices') else 0,
                num_musicians=int(data.get('num_musicians', 1)) if data.get('num_musicians') else 0,
                dress_code=data.get('dress_code'),
                client_name=data.get('client_name'),
                client_phone=data.get('client_phone'),
                client_email=data.get('client_email'),
                contact_method=data.get('contact_method'),
                comments=data.get('comments'),
                calculation_log=calculation_log_str, # Save the log
                **pricing_breakdown 
            )
            
            # --- Associate a program ---
            # Now we use an existing program or create a new one if specified
            # This logic can be extended in the future, for now it will just link or create new
            if not new_quote.program:
                program = Program.objects.create(name=f"Programa para {new_quote.tracking_code}")
                new_quote.program = program

            new_quote.save()

            # --- 3. Send email ---
            if new_quote.client_email:
                try:
                    email_context = {'quote': new_quote}
                    html_message = render_to_string('emails/quote_confirmation.html', email_context)
                    plain_message = render_to_string('emails/quote_confirmation.txt', email_context)
                    send_mail(
                        subject=f'Confirmación de Cotización Coralia: #{new_quote.tracking_code}',
                        message=plain_message,
                        from_email=None,
                        recipient_list=[new_quote.client_email, 'pedromartinezdelpaso@gmail.com'],
                        html_message=html_message,
                    )
                except Exception as e:
                    # Log email sending errors, but don't crash the user's experience
                    print(f"Error sending email for quote {new_quote.tracking_code}: {e}")

            return redirect(reverse('quotes:ver_cotizacion', args=[new_quote.tracking_code]))
    else:
        form = QuoteForm()

    tracker_form = TrackerForm()
    packages = Package.objects.filter(is_active=True)
    return render(request, 'quotes/cotizador.html', {'form': form, 'tracker_form': tracker_form, 'packages': packages})


def ver_cotizacion_view(request, code):
    code = code.lower()
    quote = get_object_or_404(Quote, tracking_code=code)
    return render(request, 'quotes/ver_cotizacion.html', {'quote': quote})


def cotizacion_detail_view(request, code):
    """
    This is the full detail page for a tracked quote.
    """
    code = code.lower()
    # Eagerly load the related program and its items to improve performance
    quote = get_object_or_404(Quote.objects.select_related('program', 'package', 'event_type'), tracking_code=code)
    
    program_items = []
    if quote.program:
        # Also fetch the related repertoire pieces in the same query
        program_items = quote.program.items.select_related('repertoire_piece').order_by('order')

    context = {
        'quote': quote,
        'program_items': program_items,
        # Show payment info if the quote is still active
        'show_payment_info': quote.status in ['UNCONFIRMED', 'CONFIRMED'],
    }
    # This render call will now work because the template syntax is fixed
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
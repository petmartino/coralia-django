import uuid
import base58
import math
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Quote
from .forms import QuoteForm, TrackerForm

def generate_tracking_code():
    while True:
        code = base58.b58encode(uuid.uuid4().bytes).decode('utf-8')[:8]
        if not Quote.objects.filter(tracking_code=code).exists():
            return code

def cotizador_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # --- 1. GET DATA FROM FORM ---
            data = form.cleaned_data

            # --- 2. PRICING VARIABLES ---
            PRICE_MUSICIAN_BASE_WEEKDAY = 800.0
            PRICE_MUSICIAN_BASE_WEEKEND = 900.0
            PRICE_GALA_ATTIRE_PER_PERSON = 250.0
            PRICE_PRIME_TIME_PER_PERSON = 100.0
            PRICE_DISTANCE_PER_HOUR_PER_PERSON = 300.0
            
            FEE_MANAGER_BASE_REGULAR = 200.0
            FEE_MANAGER_BASE_FUNERAL = 100.0
            FEE_MANAGER_PER_PERSON = 50.0
            FEE_MANAGER_EXTERIOR = 200.0
            FEE_MANAGER_BODA = 200.0
            FEE_CAR_PER_CAR = 350.0
            
            # --- 3. CALCULATE THE QUOTE ---
            num_voices = int(data.get('num_voices', 1))
            num_musicians = int(data.get('num_musicians', 1))
            total_people = num_voices + num_musicians
            breakdown = {}

            event_date = data.get('event_date')
            event_type = data.get('event_type')
            is_weekend = False
            weekday = -1
            if event_date:
                weekday = event_date.weekday() # Monday is 0
                if weekday >= 4: # Fri, Sat, Sun
                    is_weekend = True
            
            # A. Musician Payout Per Person
            musician_base_rate = PRICE_MUSICIAN_BASE_WEEKEND if is_weekend else PRICE_MUSICIAN_BASE_WEEKDAY
            if event_type in ["Misas de cuerpo presente", "Aniversarios luctuosos", "Triduo"]:
                musician_base_rate = PRICE_MUSICIAN_BASE_WEEKDAY
            
            breakdown['cost_musicians_base'] = musician_base_rate * total_people
            per_person_payout = musician_base_rate

            if data.get('dress_code') == "Gala":
                per_person_payout += PRICE_GALA_ATTIRE_PER_PERSON
            breakdown['cost_gala_fee'] = (per_person_payout - musician_base_rate) * total_people

            event_time_obj = data.get('event_time')
            is_prime_time = False
            if event_time_obj and is_weekend and weekday in [4, 5]: # Fri or Sat
                if event_time_obj >= datetime.strptime("17:00", "%H:%M").time() and event_time_obj <= datetime.strptime("20:00", "%H:%M").time():
                    is_prime_time = True
                    per_person_payout += PRICE_PRIME_TIME_PER_PERSON
            breakdown['cost_primetime_fee'] = PRICE_PRIME_TIME_PER_PERSON * total_people if is_prime_time else 0.0

            distance_hours = 0
            location_type = data.get('location_type')
            if location_type == "1_hora": distance_hours = 1
            elif location_type == "2_horas": distance_hours = 2
            elif location_type == "3_horas": distance_hours = 3
            per_person_payout += distance_hours * PRICE_DISTANCE_PER_HOUR_PER_PERSON
            breakdown['cost_distance_fee'] = (distance_hours * PRICE_DISTANCE_PER_HOUR_PER_PERSON) * total_people

            rounded_per_person_payout = math.ceil(per_person_payout / 50.0) * 50.0
            breakdown['total_musician_payout_rounded'] = rounded_per_person_payout * total_people

            # B. Manager & Logistics Fees
            if event_type in ["Misas de cuerpo presente", "Triduo"]:
                breakdown['cost_manager_base'] = FEE_MANAGER_BASE_FUNERAL
            else:
                breakdown['cost_manager_base'] = FEE_MANAGER_BASE_REGULAR
            breakdown['cost_manager_per_person'] = FEE_MANAGER_PER_PERSON * total_people
            breakdown['cost_manager_exterior'] = FEE_MANAGER_EXTERIOR if data.get('is_exterior') else 0.0
            breakdown['cost_manager_boda'] = FEE_MANAGER_BODA if event_type == "Bodas" else 0.0

            num_cars = 0
            if distance_hours > 0 and total_people > 0:
                num_cars = math.ceil(total_people / 3.0)
            breakdown['cost_car_fee'] = num_cars * FEE_CAR_PER_CAR

            # C. Calculate Final Total
            total_cost = (
                breakdown['total_musician_payout_rounded'] +
                breakdown['cost_manager_base'] +
                breakdown['cost_manager_per_person'] +
                breakdown['cost_manager_exterior'] +
                breakdown['cost_manager_boda'] +
                breakdown['cost_car_fee']
            )

            # --- 4. SAVE TO DATABASE ---
            new_quote = Quote(
                tracking_code=generate_tracking_code(),
                event_date=data.get('event_date'),
                event_time=data.get('event_time'),
                event_type=data.get('event_type'),
                location_type=data.get('location_type'),
                is_exterior=data.get('is_exterior', False),
                num_voices=num_voices,
                num_musicians=num_musicians,
                dress_code=data.get('dress_code'),
                client_name=data.get('client_name'),
                client_phone=data.get('client_phone'),
                client_email=data.get('client_email'),
                contact_method=data.get('contact_method'),
                comments=data.get('comments'),
                **breakdown,
                total_cost=total_cost,
            )
            new_quote.save()

            return redirect(reverse('quotes:ver_cotizacion', args=[new_quote.tracking_code]))
    else:
        form = QuoteForm()

    tracker_form = TrackerForm()
    return render(request, 'quotes/cotizador.html', {'form': form, 'tracker_form': tracker_form})

def ver_cotizacion_view(request, code):
    quote = get_object_or_404(Quote, tracking_code=code)
    return render(request, 'quotes/ver_cotizacion.html', {'quote': quote})

def rastrear_cotizacion_view(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('tracking_code')
            quote = Quote.objects.filter(tracking_code=code).first()
            if quote:
                return redirect(reverse('quotes:ver_cotizacion', args=[code]))
    
    # If not found or not a POST request, redirect back to cotizador
    return redirect(reverse('quotes:cotizador'))
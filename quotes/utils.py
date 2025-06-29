# quotes/utils.py

import math
from datetime import datetime

# --- ALL PRICING CONSTANTS CENTRALIZED HERE ---
# These are fallback values if something isn't set, but logic should use DB values.
PRICE_MUSICIAN_BASE_WEEKDAY = 800.0
PRICE_MUSICIAN_BASE_WEEKEND = 900.0
PRICE_GALA_ATTIRE_PER_PERSON = 250.0
PRICE_PRIME_TIME_PER_PERSON = 100.0
PRICE_DISTANCE_PER_HOUR_PER_PERSON = 300.0

# Manager & Car Fees (can also be moved to a settings model later if needed)
FEE_MANAGER_PER_PERSON = 50.0
FEE_MANAGER_EXTERIOR = 200.0
FEE_CAR_PER_CAR = 350.0


def calculate_pricing(quote_or_form_data):
    """
    Calculates all pricing fields for a quote.
    Accepts either a Quote model instance or a cleaned form data dictionary.
    """
    from .models import Quote # Local import to prevent circular dependencies

    is_instance = isinstance(quote_or_form_data, Quote)
    data = quote_or_form_data
    
    # --- Determine total people ---
    if is_instance and data.package:
        total_people = data.package.num_singers + data.package.num_instrument_players
    elif not is_instance and data.get('package'):
        pkg = data.get('package')
        total_people = pkg.num_singers + pkg.num_instrument_players
    else:
        num_voices = int(data.num_voices if is_instance else data.get('num_voices', 1))
        num_musicians = int(data.num_musicians if is_instance else data.get('num_musicians', 1))
        total_people = num_voices + num_musicians

    breakdown = {}
    event_type = data.event_type if is_instance else data.get('event_type')

    if not event_type: # Can't calculate without an event type
        return {}
        
    # --- Base Musician Rate ---
    event_date = data.event_date if is_instance else data.get('event_date')
    is_weekend = False
    weekday = -1
    if event_date:
        weekday = event_date.weekday()
        # Friday (4), Saturday (5), Sunday (6) are weekends
        if weekday >= 4:
            is_weekend = True
    
    musician_base_rate = PRICE_MUSICIAN_BASE_WEEKEND if is_weekend else PRICE_MUSICIAN_BASE_WEEKDAY
    # Override with EventType rule
    if event_type.is_funeral_type:
        musician_base_rate = PRICE_MUSICIAN_BASE_WEEKDAY

    breakdown['cost_musicians_base'] = musician_base_rate * total_people
    per_person_payout = musician_base_rate
    
    # Weekend Fee is the difference (for display only)
    breakdown['cost_weekend_fee'] = (PRICE_MUSICIAN_BASE_WEEKEND - PRICE_MUSICIAN_BASE_WEEKDAY) * total_people if is_weekend and not event_type.is_funeral_type else 0.0

    # --- Additional Fees ---
    dress_code = data.dress_code if is_instance else data.get('dress_code')
    if dress_code == "Gala":
        per_person_payout += PRICE_GALA_ATTIRE_PER_PERSON
    breakdown['cost_gala_fee'] = (per_person_payout - musician_base_rate) * total_people

    event_time_obj = data.event_time if is_instance else data.get('event_time')
    is_prime_time = False
    # Prime time is Fri/Sat (weekday 4/5) between 5 PM and 8 PM
    if event_time_obj and is_weekend and weekday in [4, 5]:
        if event_time_obj >= datetime.strptime("17:00", "%H:%M").time() and event_time_obj <= datetime.strptime("20:00", "%H:%M").time():
            is_prime_time = True
            per_person_payout += PRICE_PRIME_TIME_PER_PERSON
    breakdown['cost_primetime_fee'] = PRICE_PRIME_TIME_PER_PERSON * total_people if is_prime_time else 0.0

    distance_hours = 0
    location_type = data.location_type if is_instance else data.get('location_type')
    if location_type == "1_hora": distance_hours = 1
    elif location_type == "2_horas": distance_hours = 2
    elif location_type == "3_horas": distance_hours = 3
    per_person_payout += distance_hours * PRICE_DISTANCE_PER_HOUR_PER_PERSON
    breakdown['cost_distance_fee'] = (distance_hours * PRICE_DISTANCE_PER_HOUR_PER_PERSON) * total_people

    rounded_per_person_payout = math.ceil(per_person_payout / 50.0) * 50.0
    breakdown['total_musician_payout_rounded'] = rounded_per_person_payout * total_people
    breakdown['payment_per_musician'] = rounded_per_person_payout # Save individual payment

    # --- Manager & Car Fees ---
    breakdown['cost_manager_base'] = event_type.manager_base_fee
    breakdown['cost_manager_per_person'] = FEE_MANAGER_PER_PERSON * total_people
    
    is_exterior = data.is_exterior if is_instance else data.get('is_exterior', False)
    breakdown['cost_manager_exterior'] = FEE_MANAGER_EXTERIOR if is_exterior else 0.0
    breakdown['cost_manager_boda'] = event_type.manager_base_fee if event_type.has_wedding_fee else 0.0

    num_cars = math.ceil(total_people / 3.0) if distance_hours > 0 and total_people > 0 else 0
    breakdown['cost_car_fee'] = num_cars * FEE_CAR_PER_CAR
    
    # --- Final Total ---
    subtotal = sum(v for k, v in breakdown.items() if k.startswith('cost_'))
    discount_val = data.discount if is_instance else data.get('discount', 0.0)
    
    breakdown['total_cost'] = subtotal - discount_val

    return breakdown
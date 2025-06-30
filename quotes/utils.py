# quotes/utils.py

import math
from datetime import datetime

# --- ALL PRICING CONSTANTS CENTRALIZED HERE ---
PRICE_MUSICIAN_BASE_WEEKDAY = 800.0
PRICE_MUSICIAN_BASE_WEEKEND = 900.0
PRICE_GALA_ATTIRE_PER_PERSON = 250.0
PRICE_PRIME_TIME_PER_PERSON = 100.0
PRICE_DISTANCE_PER_HOUR_PER_PERSON = 300.0

# Manager & Car Fees
FEE_MANAGER_PER_PERSON = 50.0
FEE_MANAGER_EXTERIOR = 200.0
FEE_CAR_PER_CAR = 350.0


def calculate_pricing(quote_or_form_data):
    """
    Calculates all pricing fields for a quote.
    Accepts either a Quote model instance or a cleaned form data dictionary.
    Returns a dictionary of costs and a string log of the calculation.
    """
    from .models import Quote # Local import to prevent circular dependencies

    is_instance = isinstance(quote_or_form_data, Quote)
    data = quote_or_form_data
    log = []
    
    # --- Determine total people ---
    if is_instance and data.package:
        pkg = data.package
        total_people = pkg.num_singers + pkg.num_instrument_players
        log.append(f"Paquete seleccionado: '{pkg.name}' con {total_people} personas.")
    elif not is_instance and data.get('package'):
        pkg = data.get('package')
        total_people = pkg.num_singers + pkg.num_instrument_players
        log.append(f"Paquete seleccionado: '{pkg.name}' con {total_people} personas.")
    else:
        num_voices = int(data.num_voices if is_instance else data.get('num_voices', 1))
        num_musicians = int(data.num_musicians if is_instance else data.get('num_musicians', 1))
        total_people = num_voices + num_musicians
        log.append(f"Configuración personalizada: {num_voices} voces + {num_musicians} músicos = {total_people} personas.")

    breakdown = {}
    event_type = data.event_type if is_instance else data.get('event_type')

    if not event_type: # Can't calculate without an event type
        return {}, "No se pudo calcular el precio: Falta el tipo de evento."
        
    # --- Base Musician Rate ---
    event_date = data.event_date if is_instance else data.get('event_date')
    is_weekend = False
    weekday = -1
    if event_date:
        weekday = event_date.weekday()
        if weekday >= 4: is_weekend = True # Friday (4) to Sunday (6)
    
    musician_base_rate = PRICE_MUSICIAN_BASE_WEEKEND if is_weekend else PRICE_MUSICIAN_BASE_WEEKDAY
    rate_type_log = "fin de semana" if is_weekend else "entre semana"
    log.append(f"1. Tasa base por músico ({rate_type_log}): ${musician_base_rate:,.2f}")
    if event_type.is_funeral_type and is_weekend:
        musician_base_rate = PRICE_MUSICIAN_BASE_WEEKDAY
        log.append(f"   -> Anulación por evento funerario. Tasa forzada a: ${musician_base_rate:,.2f}")

    breakdown['cost_musicians_base'] = musician_base_rate * total_people
    per_person_payout = musician_base_rate
    
    # --- Additional Fees per person ---
    dress_code = data.dress_code if is_instance else data.get('dress_code')
    gala_fee = PRICE_GALA_ATTIRE_PER_PERSON if dress_code == "Gala" else 0
    per_person_payout += gala_fee
    log.append(f"2. Aumento por vestimenta de Gala: +${gala_fee:,.2f} por persona")

    is_prime_time = False
    prime_time_fee = 0
    if event_time_obj := (data.event_time if is_instance else data.get('event_time')):
        if is_weekend and weekday in [4, 5]:
            if event_time_obj >= datetime.strptime("17:00", "%H:%M").time() and event_time_obj <= datetime.strptime("20:00", "%H:%M").time():
                is_prime_time = True
                prime_time_fee = PRICE_PRIME_TIME_PER_PERSON
    per_person_payout += prime_time_fee
    log.append(f"3. Aumento por horario estelar (Prime Time): +${prime_time_fee:,.2f} por persona")

    distance_hours = 0
    location_type = data.location_type if is_instance else data.get('location_type')
    if location_type == "1_hora": distance_hours = 1
    elif location_type == "2_horas": distance_hours = 2
    elif location_type == "3_horas": distance_hours = 3
    distance_fee_per_person = distance_hours * PRICE_DISTANCE_PER_HOUR_PER_PERSON
    per_person_payout += distance_fee_per_person
    log.append(f"4. Aumento por distancia ({distance_hours}h): +${distance_fee_per_person:,.2f} por persona")

    log.append(f"\nSubtotal por músico (1+2+3+4): ${per_person_payout:,.2f}")
    rounded_per_person_payout = math.ceil(per_person_payout / 50.0) * 50.0
    breakdown['payment_per_musician'] = rounded_per_person_payout
    log.append(f"Pago redondeado por músico: ${rounded_per_person_payout:,.2f}")
    
    total_musician_cost = rounded_per_person_payout * total_people
    log.append(f"A. COSTO TOTAL DE MÚSICOS ({total_people} x ${rounded_per_person_payout:,.2f}) = ${total_musician_cost:,.2f}")
    
    # --- Manager & Car Fees ---
    manager_base = event_type.manager_base_fee
    log.append(f"B. Tarifa base de gestión: +${manager_base:,.2f}")

    manager_per_person_fee = FEE_MANAGER_PER_PERSON * total_people
    log.append(f"C. Tarifa de gestión por músico ({total_people} x ${FEE_MANAGER_PER_PERSON:,.2f}): +${manager_per_person_fee:,.2f}")
    
    is_exterior = data.is_exterior if is_instance else data.get('is_exterior', False)
    manager_exterior_fee = FEE_MANAGER_EXTERIOR if is_exterior else 0.0
    log.append(f"D. Tarifa por evento en exterior: +${manager_exterior_fee:,.2f}")

    manager_wedding_fee = event_type.manager_base_fee if event_type.has_wedding_fee else 0.0
    log.append(f"E. Tarifa especial de boda: +${manager_wedding_fee:,.2f}")

    num_cars = math.ceil(total_people / 4.0) if distance_hours > 0 and total_people > 0 else 0
    car_total_fee = num_cars * FEE_CAR_PER_CAR
    log.append(f"F. Tarifa de transporte ({num_cars} coches): +${car_total_fee:,.2f}")

    # --- Final Total ---
    subtotal = (
        total_musician_cost + manager_base + manager_per_person_fee + 
        manager_exterior_fee + manager_wedding_fee + car_total_fee
    )
    log.append(f"\nSUBTOTAL (A+B+C+D+E+F): ${subtotal:,.2f}")
    
    discount_val = data.discount if is_instance else data.get('discount', 0.0)
    if not is_instance:
        breakdown['discount'] = discount_val
    log.append(f"Descuento aplicado: -${discount_val:,.2f}")
    
    # Set all breakdown fields
    breakdown.update({
        'cost_musicians_base': total_musician_cost, # Note: this is the rounded total now
        'cost_weekend_fee': (PRICE_MUSICIAN_BASE_WEEKEND - PRICE_MUSICIAN_BASE_WEEKDAY) * total_people if is_weekend and not event_type.is_funeral_type else 0.0,
        'cost_gala_fee': gala_fee * total_people,
        'cost_primetime_fee': prime_time_fee * total_people,
        'cost_distance_fee': distance_fee_per_person * total_people,
        'total_musician_payout_rounded': total_musician_cost,
        'cost_manager_base': manager_base,
        'cost_manager_per_person': manager_per_person_fee,
        'cost_manager_exterior': manager_exterior_fee,
        'cost_manager_boda': manager_wedding_fee,
        'cost_car_fee': car_total_fee
    })
    
    breakdown['total_cost'] = subtotal - discount_val
    log.append(f"COSTO TOTAL FINAL: ${breakdown['total_cost']:,.2f}")

    return breakdown, "\n".join(log)
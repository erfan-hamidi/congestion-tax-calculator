from datetime import datetime, timedelta

TOLL_FREE_VEHICLES = ["Motorbike", "Tractor", "Emergency", "Diplomat", "Foreign", "Military"]

def is_toll_free_vehicle(vehicle):
    return vehicle.vehicle_type in TOLL_FREE_VEHICLES

def is_toll_free_date(date):
    if date.weekday() >= 5:  # Saturday or Sunday
        return True

    # All days in July  
    if date.month == 7:
        return True

    toll_free_dates = [
        (1, 1), (3, 28), (3, 29), (4, 1), (4, 30), (5, 1),
        (5, 8), (5, 9), (6, 5), (6, 6), (6, 21), (11, 1),
        (12, 24), (12, 25), (12, 26), (12, 31)
    ]

    return (date.month, date.day) in toll_free_dates

def get_toll_fee(date, vehicle):
    if is_toll_free_date(date) or is_toll_free_vehicle(vehicle):
        return 0

    hour, minute = date.hour, date.minute

    if hour == 6 and minute <= 29:
        return 8
    if hour == 6 and minute <= 59:
        return 13
    if hour == 7:
        return 18
    if hour == 8 and minute <= 29:
        return 13
    if 8 <= hour <= 14:
        return 8
    if hour == 15 and minute <= 29:
        return 13
    if hour == 15 or hour == 16:
        return 18
    if hour == 17:
        return 13
    if hour == 18 and minute <= 29:
        return 8
    return 0

def calculate_congestion_tax(vehicle, dates):
    if not dates:
        return 0

    total_fee = 0
    interval_start = dates[0]

    for date in dates:
        next_fee = get_toll_fee(date, vehicle)
        temp_fee = get_toll_fee(interval_start, vehicle)

        if (date - interval_start).total_seconds() / 60 <= 60:
            if total_fee > 0:
                total_fee -= temp_fee
            if next_fee >= temp_fee:
                temp_fee = next_fee
            total_fee += temp_fee
        else:
            total_fee += next_fee
            interval_start = date

    return min(total_fee, 60)


# def calculate_congestion_tax(vehicle_type, timestamps, tax_rules):
#     # Implement your congestion tax calculation logic here
#     # This function should return the calculated tax based on the vehicle type, timestamps, and tax rules
#     total_tax = 0
#     # Example implementation (replace with actual logic)
#     for timestamp in timestamps:
#         for rule in tax_rules:
#             if rule.start_time <= timestamp.time() <= rule.end_time:
#                 total_tax += rule.amount
#                 break
#     return min(total_tax, 60)  # Maximum tax per day is 60 SEK

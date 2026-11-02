

from datetime import datetime


rates = {
    "bike": 10,
    "car": 20,
    "bus": 40
}


daily_limits = {
    "bike": 100,
    "car": 200,
    "bus": 400
}


penalty_rate = 50


def validate_time(time):
    try:
        return datetime.strptime(time, "%H:%M")
    except ValueError:
        return None


print("===== SMART PARKING FEE MANAGEMENT =====")


vehicle_number = input("Enter vehicle number: ").upper()

vehicle_type = input(
    "Enter vehicle type (Bike/Car/Bus): "
).lower()

if vehicle_type not in rates:
    print("Invalid vehicle category!")
    exit()


while True:
    entry_time = input("Enter entry time (HH:MM): ")
    entry = validate_time(entry_time)

    if entry:
        break
    else:
        print("Invalid entry time! Enter again.")


while True:
    exit_time = input("Enter exit time (HH:MM): ")
    exit = validate_time(exit_time)

    if exit:
        break
    else:
        print("Invalid exit time! Enter again.")


entry_minutes = entry.hour * 60 + entry.minute
exit_minutes = exit.hour * 60 + exit.minute


if exit_minutes < entry_minutes:
    duration = (1440 - entry_minutes) + exit_minutes
    print("\nOvernight parking detected.")
else:
    duration = exit_minutes - entry_minutes


total_hours = (duration + 59) // 60


hourly_rate = rates[vehicle_type]
basic_fee = total_hours * hourly_rate


daily_limit = daily_limits[vehicle_type]

if total_hours <= 24:
    parking_fee = min(basic_fee, daily_limit)
else:
    full_days = total_hours // 24
    remaining_hours = total_hours % 24

    parking_fee = (
        full_days * daily_limit
        + min(remaining_hours * hourly_rate, daily_limit)
    )


penalty = 0

if total_hours > 24:
    penalty = penalty_rate


total_fee = parking_fee + penalty


print("\n========== PARKING BILL ==========")
print("Vehicle Number :", vehicle_number)
print("Vehicle Type   :", vehicle_type.capitalize())
print("Entry Time     :", entry_time)
print("Exit Time      :", exit_time)
print("Duration       :", duration // 60,
      "hours", duration % 60, "minutes")
print("Billable Hours :", total_hours)
print("Hourly Rate    : Rs.", hourly_rate)
print("Parking Fee    : Rs.", parking_fee)
print("Penalty        : Rs.", penalty)
print("----------------------------------")
print("Total Fee      : Rs.", total_fee)
print("==================================")

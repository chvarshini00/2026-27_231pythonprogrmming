

import math


print("--- CAMPUS EVENT FINANCIAL PLANNING ---")

participants = int(input("Enter expected number of participants: "))


venue = float(input("Enter venue rental cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
transport = float(input("Enter transportation cost: Rs. "))


catering = float(input("Enter catering cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))


sponsorship_target = float(input("Enter sponsorship target: Rs. "))
sponsorship_received = float(input("Enter sponsorship received: Rs. "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))


total_catering = participants * catering
total_certificate = participants * certificate

fixed_cost = venue + equipment + transport

variable_cost = total_catering + total_certificate

total_expenses = fixed_cost + variable_cost

participant_contribution = participants * registration_fee


sponsorship_shortfall = max(
    0, sponsorship_target - sponsorship_received
)

total_income = participant_contribution + sponsorship_received


balance = total_income - total_expenses


cost_per_participant = catering + certificate

contribution_margin = registration_fee - cost_per_participant

remaining_fixed_cost = max(0, fixed_cost - sponsorship_received)

if remaining_fixed_cost == 0:
    break_even = 0

elif contribution_margin > 0:
    break_even = math.ceil(
        remaining_fixed_cost / contribution_margin
    )

else:
    break_even = None


print("\n--- EVENT EXPENSE DETAILS ---")

print(f"Venue Cost: Rs.{venue:.2f}")
print(f"Equipment Cost: Rs.{equipment:.2f}")
print(f"Transportation Cost: Rs.{transport:.2f}")
print(f"Total Catering Cost: Rs.{total_catering:.2f}")
print(f"Total Certificate Cost: Rs.{total_certificate:.2f}")

print(f"\nTotal Fixed Cost: Rs.{fixed_cost:.2f}")
print(f"Total Variable Cost: Rs.{variable_cost:.2f}")
print(f"Total Event Expenses: Rs.{total_expenses:.2f}")

print("\n--- EVENT INCOME DETAILS ---")

print(f"Participant Contributions: Rs.{participant_contribution:.2f}")
print(f"Sponsorship Received: Rs.{sponsorship_received:.2f}")
print(f"Total Income: Rs.{total_income:.2f}")

print(f"Sponsorship Target: Rs.{sponsorship_target:.2f}")
print(f"Sponsorship Shortfall: Rs.{sponsorship_shortfall:.2f}")


print("\n--- FINANCIAL SUMMARY ---")

if balance > 0:
    print(f"Expected Profit: Rs.{balance:.2f}")

elif balance < 0:
    print(f"Expected Loss: Rs.{abs(balance):.2f}")

else:
    print("Event is at break-even point.")

print("\n--- BREAK-EVEN ANALYSIS ---")

if break_even is not None:
    print("Minimum registrations required:", break_even)

    if participants >= break_even:
        print("Expected registrations are sufficient.")
    else:
        print("Additional registrations required:",
              break_even - participants)

else:
    print("Break-even cannot be achieved through registrations alone.")
    print("Increase registration fee or sponsorship.")

print("\nEvent financial planning completed.")

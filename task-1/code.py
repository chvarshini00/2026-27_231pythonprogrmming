

plans = []

n = int(input("Enter number of mobile plans: "))


for i in range(n):
    print(f"\nEnter details of Plan {i+1}")

    name = input("Plan name: ")
    price = float(input("Base price: "))
    data = float(input("Included data (GB): "))
    calls = int(input("Included call minutes: "))
    sms = int(input("Included SMS: "))
    validity = int(input("Validity (days): "))

    extra_data = float(input("Extra data charge per GB: "))
    extra_call = float(input("Extra call charge per minute: "))
    extra_sms = float(input("Extra SMS charge per message: "))

    plans.append((name, price, data, calls, sms,
                  validity, extra_data, extra_call, extra_sms))


print("\n--- USER REQUIREMENTS ---")

req_data = float(input("Required data (GB): "))
req_calls = int(input("Required call minutes: "))
req_sms = int(input("Required SMS: "))
req_validity = int(input("Required validity (days): "))
budget = float(input("Maximum budget: "))

eligible_plans = []


print("\n--- PLAN COST ANALYSIS ---")

for plan in plans:

    name, price, data, calls, sms, validity, \
    extra_data, extra_call, extra_sms = plan


    excess_data = max(0, req_data - data)
    excess_calls = max(0, req_calls - calls)
    excess_sms = max(0, req_sms - sms)

    
    data_charge = excess_data * extra_data
    call_charge = excess_calls * extra_call
    sms_charge = excess_sms * extra_sms

    total_cost = price + data_charge + call_charge + sms_charge

    print(f"\nPlan: {name}")
    print(f"Base Price: Rs.{price:.2f}")
    print(f"Excess Data Charge: Rs.{data_charge:.2f}")
    print(f"Excess Call Charge: Rs.{call_charge:.2f}")
    print(f"Excess SMS Charge: Rs.{sms_charge:.2f}")
    print(f"Total Cost: Rs.{total_cost:.2f}")

    
    if validity >= req_validity and total_cost <= budget:

        print("Status: Eligible")

        eligible_plans.append((total_cost, name))

    else:
        print("Status: Not Eligible")


print("\n--- FINAL RESULT ---")

if eligible_plans:

    best_plan = min(eligible_plans)

    print("Most Economical Plan:", best_plan[1])
    print(f"Total Cost: Rs.{best_plan[0]:.2f}")

else:
    print("No eligible mobile plan found.")

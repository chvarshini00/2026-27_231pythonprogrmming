venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: "))


fixed_cost = venue + equipment + transport
variable_cost = catering + certificate

total_cost = fixed_cost + (variable_cost * participants)


contribution = total_cost / participants


shortfall = max(0, total_cost - sponsorship)


if contribution > variable_cost:
    minimum = int(fixed_cost / (contribution - variable_cost))
    if minimum * (contribution - variable_cost) < fixed_cost:
        minimum += 1
else:
    minimum = 0

print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
print("Fixed Cost:", fixed_cost)
print("Total Event Cost:", total_cost)
print("Participant Contribution:", contribution)
print("Sponsorship Shortfall:", shortfall)
print("Minimum Registrations:", minimum)

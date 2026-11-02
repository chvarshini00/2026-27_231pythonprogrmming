distance = float(input("Enter travel distance in km: "))
n = int(input("Enter number of passengers: "))

rate = 2.0
total = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    category = input("Enter category (Normal/Child/Senior): ").lower()

    fare = distance * rate

    if category == "child":
        fare = fare * 0.5

    elif category == "senior":
        fare = fare * 0.8

    total += fare

    print("Passenger Name:", name)
    print("Ticket Fare:", fare)

print("\nTotal Reservation Cost:", total)

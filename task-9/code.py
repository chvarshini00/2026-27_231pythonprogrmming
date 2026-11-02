import math

print("===== ROUTE DISTANCE ANALYSIS =====")


n = int(input("Enter number of locations: "))

locations = []

for i in range(n):
    print("\nEnter coordinates for Location", i + 1)

    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    coordinates = (latitude, longitude)

    locations.append(coordinates)

if n < 2:
    print("\nAt least two locations are required.")

else:
    max_distance = 0
    longest_segment = None

    print("\n========== ROUTE SEGMENT DISTANCES ==========")

    for i in range(n - 1):

        # Extract coordinates from tuples
        x1, y1 = locations[i]
        x2, y2 = locations[i + 1]

        # Euclidean distance formula
        distance = math.sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        )

        print(
            "Location", i + 1, "to Location", i + 2,
            ":", round(distance, 2)
        )

        if distance > max_distance:
            max_distance = distance
            longest_segment = (i + 1, i + 2)

    print("\nStored Coordinate Tuples:")
    for i, point in enumerate(locations):
        print("Location", i + 1, ":", point)

    print("\n========== LONGEST ROUTE SEGMENT ==========")

    print(
        "Longest Segment: Location",
        longest_segment[0],
        "to Location",
        longest_segment[1]
    )

    print("Maximum Distance:", round(max_distance, 2))

print("\nRoute analysis completed.")

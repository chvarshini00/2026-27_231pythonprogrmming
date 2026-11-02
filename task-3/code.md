# Smart Parking Fee Management System

## 1. Problem Statement

Develop a Python program for a Smart Parking Fee Management System that calculates parking charges based on vehicle entry and exit times, vehicle categories, overnight parking, daily parking limits, and penalty conditions.

The program should:

- Accept vehicle registration number and vehicle category.
- Validate entry and exit times in 24-hour format.
- Calculate total parking duration, including overnight parking.
- Apply different hourly rates for cars, bikes, and buses.
- Calculate parking fees based on the vehicle category.
- Apply daily maximum parking limits.
- Add penalties for invalid conditions, such as exceeding the permitted parking duration.
- Display the total parking duration, basic fee, penalty, and final parking charge.

## 2. Algorithm

1. Start the program.
2. Define hourly parking rates for different vehicle categories.
3. Define the maximum daily parking charge.
4. Read the vehicle registration number.
5. Read the vehicle category (Bike, Car, or Bus).
6. Read entry time and exit time in HH:MM format.
7. Validate the entered time values.
8. Convert entry and exit times into minutes.
9. If exit time is earlier than entry time, consider the parking duration as overnight.
10. Calculate the total parking duration in hours.
11. Calculate the parking fee using the vehicle category's hourly rate.
12. Apply the maximum daily parking limit.
13. Check whether the parking duration exceeds 24 hours.
14. If it exceeds 24 hours, calculate the additional penalty.
15. Calculate the final parking fee.
16. Display vehicle details, parking duration, basic fee, penalty, and total fee.
17. Stop.



## 5. Sample Input

```
===== SMART PARKING FEE MANAGEMENT =====
Enter vehicle number: AP39AB1234
Enter vehicle type (Bike/Car/Bus): Car
Enter entry time (HH:MM): 20:30
Enter exit time (HH:MM): 02:30
```

## 6. Sample Output

```
Overnight parking detected.

========== PARKING BILL ==========
Vehicle Number : AP39AB1234
Vehicle Type   : Car
Entry Time     : 20:30
Exit Time      : 02:30
Duration       : 6 hours 0 minutes
Billable Hours : 6
Hourly Rate    : Rs. 20
Parking Fee    : Rs. 120
Penalty        : Rs. 0
----------------------------------
Total Fee      : Rs. 120
==================================
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Define Vehicle Rates and Daily Limits]
    B --> C[/Enter Vehicle Number/]
    C --> D[/Enter Vehicle Category/]
    D --> E{Valid Vehicle Category?}

    E -- No --> F[Display Invalid Category]
    F --> Z([Stop])

    E -- Yes --> G[/Enter Entry Time/]
    G --> H{Valid Entry Time?}
    H -- No --> G
    H -- Yes --> I[/Enter Exit Time/]

    I --> J{Valid Exit Time?}
    J -- No --> I
    J -- Yes --> K[Convert Times into Minutes]

    K --> L{Exit Earlier than Entry?}
    L -- Yes --> M[Calculate Overnight Duration]
    L -- No --> N[Calculate Same-Day Duration]

    M --> O[Calculate Total Hours]
    N --> O

    O --> P[Calculate Basic Parking Fee]
    P --> Q[Apply Daily Maximum Limit]

    Q --> R{Parking More Than 24 Hours?}
    R -- Yes --> S[Calculate Additional Penalty]
    R -- No --> T[Penalty = 0]

    S --> U[Calculate Final Parking Fee]
    T --> U

    U --> V[/Display Parking Bill/]
    V --> Z([Stop])
mermaid


```



## 8. Expected Concepts Used

| Concept                | Application                          |
| ---------------------- | ------------------------------------ |
| Variables              | Store vehicle and time details       |
| Dictionary             | Store vehicle rates and daily limits |
| Conditional statements | Check vehicle type and penalties     |
| While loop             | Validate time inputs                 |
| Functions              | Validate time format                 |
| Arithmetic operations  | Calculate duration and fees          |
| Type conversion        | Convert time into minutes            |



I can also create an image explaining the complete parking fee management flowchart.

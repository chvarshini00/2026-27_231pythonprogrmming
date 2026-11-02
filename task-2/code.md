# Campus Event Financial Planning

## 1. Problem Statement

Develop a Python program to manage the financial planning of a campus event by calculating expenses, participant contributions, sponsorship requirements, and the minimum number of registrations needed to break even.

The program should perform the following operations:

- Accept venue rental costs.
- Calculate equipment expenses.
- Calculate catering costs based on the number of participants.
- Calculate transportation expenses.
- Calculate certificate printing costs.
- Calculate the total event expenditure.
- Determine the contribution required from each participant.
- Calculate the sponsorship amount received and identify any sponsorship shortfall.
- Determine the minimum registration count required to break even.
- Display a complete financial summary.

The objective is to plan the event budget efficiently and ensure that the total expected income covers all event expenses.

## 2. Algorithm

1. Start the program.
2. Read the number of expected participants.
3. Accept the venue rental cost.
4. Accept equipment expenses.
5. Accept catering cost per participant.
6. Accept transportation expenses.
7. Accept certificate cost per participant.
8. Accept the sponsorship amount received.
9. Accept the registration contribution per participant.
10. Calculate total catering expenses.
11. Calculate total certificate expenses.
12. Calculate the total event expenditure by adding all expenses.
13. Calculate the total participant contribution.
14. Calculate the sponsorship shortfall, if the sponsorship target is not achieved.
15. Calculate the remaining amount to be covered by registrations after sponsorship.
16. Calculate the minimum registration count required to break even.
17. Compare the expected registration count with the break-even registration count.
18. Display all expenses, contributions, sponsorship details, and break-even information.
19. Stop the program.

## 5. Python Source Code

```
print(f"Total Certificate Cost: Rs.{total_certificate:.2f}")print(f"\nTotal Fixed Cost: Rs.{fixed_cost:.2f}")print(f"Total Variable Cost: Rs.{variable_cost:.2f}")print(f"Total Event Expenses: Rs.{total_expenses:.2f}")# Display income detailsprint("\n--- EVENT INCOME DETAILS ---")print(f"Participant Contributions: Rs.{participant_contribution:.2f}")print(f"Sponsorship Received: Rs.{sponsorship_received:.2f}")print(f"Total Income: Rs.{total_income:.2f}")print(f"Sponsorship Target: Rs.{sponsorship_target:.2f}")print(f"Sponsorship Shortfall: Rs.{sponsorship_shortfall:.2f}")# Display profit or lossprint("\n--- FINANCIAL SUMMARY ---")if balance > 0:    print(f"Expected Profit: Rs.{balance:.2f}")elif balance < 0:    print(f"Expected Loss: Rs.{abs(balance):.2f}")else:    print("Event is at break-even point.")# Display break-even detailsprint("\n--- BREAK-EVEN ANALYSIS ---")if break_even is not None:    print("Minimum registrations required:", break_even)    if participants >= break_even:        print("Expected registrations are sufficient.")    else:        print("Additional registrations required:",              break_even - participants)else:    print("Break-even cannot be achieved through registrations alone.")    print("Increase registration fee or sponsorship.")print("\nEvent financial planning completed.")
```

## 6. Sample Input

Consider a campus technical event with 100 expected participants.

```
--- CAMPUS EVENT FINANCIAL PLANNING ---

Enter expected number of participants: 100

Enter venue rental cost: Rs. 20000
Enter equipment cost: Rs. 10000
Enter transportation cost: Rs. 5000

Enter catering cost per participant: Rs. 150
Enter certificate cost per participant: Rs. 20

Enter sponsorship target: Rs. 25000
Enter sponsorship received: Rs. 18000

Enter registration fee per participant: Rs. 300
```

## 7. Sample Output

```
--- EVENT EXPENSE DETAILS ---

Venue Cost: Rs.20000.00
Equipment Cost: Rs.10000.00
Transportation Cost: Rs.5000.00
Total Catering Cost: Rs.15000.00
Total Certificate Cost: Rs.2000.00

Total Fixed Cost: Rs.35000.00
Total Variable Cost: Rs.17000.00
Total Event Expenses: Rs.52000.00

--- EVENT INCOME DETAILS ---

Participant Contributions: Rs.30000.00
Sponsorship Received: Rs.18000.00
Total Income: Rs.48000.00

Sponsorship Target: Rs.25000.00
Sponsorship Shortfall: Rs.7000.00

--- FINANCIAL SUMMARY ---

Expected Loss: Rs.4000.00

--- BREAK-EVEN ANALYSIS ---

Minimum registrations required: 131
Additional registrations required: 31

Event financial planning completed.
```

## 8. Mermaid Flowchart Code
`` mermaid

flowchart TD
    A([Start]) --> B[/Enter expected participants/]
    B --> C[/Input venue, equipment and transport costs/]
    C --> D[/Input catering and certificate costs per participant/]
    D --> E[/Input sponsorship target and amount received/]
    E --> F[/Input registration fee/]
    F --> G[Calculate total catering and certificate costs]
    G --> H[Calculate fixed and variable expenses]
    H --> I[Calculate total event expenses]
    I --> J[Calculate participant contributions]
    J --> K[Calculate sponsorship shortfall]
    K --> L[Calculate total income and profit or loss]
    L --> M[Calculate contribution margin]
    M --> N{Fixed cost covered by sponsorship?}
    N -->|Yes| O[Break-even registrations = 0]
    N -->|No| P{Contribution margin positive?}
    P -->|Yes| Q[Calculate minimum break-even registrations]
    P -->|No| R[Break-even not achievable]
    O --> S[Display financial report]
    Q --> S
    R --> S
    S --> T([Stop])
mermaid



``




## 9. Result

The Python program successfully performs campus event financial planning by calculating venue, equipment, catering, transportation, and certificate expenses.

It determines total participant contributions, sponsorship shortfalls, expected profit or loss, and the minimum registration count required to break even.

Time Complexity: \\(O(1)\\), because the program performs a fixed number of arithmetic operations.

Space Complexity: \\(O(1)\\), because it uses a fixed number of variables.

Conclusion: The program helps educational institutions plan campus event budgets, manage expenses, estimate sponsorship requirements, and determine the minimum registrations needed to achieve financial break-even.

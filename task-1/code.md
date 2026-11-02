# Multi-Plan Telecommunications Cost Optimization

## 1. Problem Statement

Develop a Python program to evaluate multiple mobile telecommunications plans based on data usage, call minutes, SMS usage, validity period, and budget constraints.

The program should perform the following operations:

- Accept details of multiple mobile plans.
- Read the user's required data, call minutes, SMS count, and validity period.
- Calculate excess charges when usage exceeds the plan limits.
- Check whether each plan satisfies the user's budget and validity requirements.
- Identify eligible plans.
- Compare the total costs of eligible plans.
- Display the most economical mobile plan.

The objective is to minimize telecommunications expenses while satisfying all user requirements.

## 2. Algorithm

1. Start the program.
2. Read the number of available mobile plans.
3. Accept the following details for each plan:
   - Plan name
   - Base price
   - Included data limit (GB)
   - Included call minutes
   - Included SMS count
   - Validity period (days)
   - Extra data charge per GB
   - Extra call charge per minute
   - Extra SMS charge per message
4. Read the user's required data, call minutes, SMS count, validity, and budget.
5. Initialize an empty list to store eligible plans.
6. For each mobile plan:
   - Calculate excess data usage.
   - Calculate excess call minutes.
   - Calculate excess SMS usage.
   - Calculate additional charges.
   - Calculate the total plan cost.
7. Check whether the plan satisfies the validity requirement.
8. Check whether the total cost is within the user's budget.
9. If both conditions are satisfied, add the plan to the eligible plans list.
10. Compare the total costs of all eligible plans.
11. Identify the plan with the minimum total cost.
12. Display the cost details of all plans.
13. Display the most economical eligible plan.
14. If no plan is eligible, display an appropriate message.
15. Stop the program.


## 5. Sample Input

Consider three mobile plans with different data, calling, SMS, and validity limits.

```
Enter number of mobile plans: 3

Enter details of Plan 1
Plan name: Basic
Base price: 199
Included data (GB): 2
Included call minutes: 500
Included SMS: 100
Validity (days): 28
Extra data charge per GB: 50
Extra call charge per minute: 1
Extra SMS charge per message: 1

Enter details of Plan 2
Plan name: Standard
Base price: 299
Included data (GB): 5
Included call minutes: 1000
Included SMS: 200
Validity (days): 28
Extra data charge per GB: 40
Extra call charge per minute: 1
Extra SMS charge per message: 1

Enter details of Plan 3
Plan name: Premium
Base price: 399
Included data (GB): 10
Included call minutes: 1500
Included SMS: 300
Validity (days): 56
Extra data charge per GB: 30
Extra call charge per minute: 1
Extra SMS charge per message: 1

--- USER REQUIREMENTS ---
Required data (GB): 6
Required call minutes: 1200
Required SMS: 250
Required validity (days): 28
Maximum budget: 500
```

## 6. Sample Output

```
--- PLAN COST ANALYSIS ---

Plan: Basic
Base Price: Rs.199.00
Excess Data Charge: Rs.200.00
Excess Call Charge: Rs.700.00
Excess SMS Charge: Rs.150.00
Total Cost: Rs.1249.00
Status: Not Eligible

Plan: Standard
Base Price: Rs.299.00
Excess Data Charge: Rs.40.00
Excess Call Charge: Rs.200.00
Excess SMS Charge: Rs.50.00
Total Cost: Rs.589.00
Status: Not Eligible

Plan: Premium
Base Price: Rs.399.00
Excess Data Charge: Rs.0.00
Excess Call Charge: Rs.0.00
Excess SMS Charge: Rs.0.00
Total Cost: Rs.399.00
Status: Eligible

--- FINAL RESULT ---
Most Economical Plan: Premium
Total Cost: Rs.399.00
```

## 7. Mermaid Flowchart Code
``` mermaid
    flowchart TD
    A([Start]) --> B[/Enter number of mobile plans/]
    B --> C[Initialize plans list]
    C --> D[/Enter plan details/]
    D --> E[Store plan details]
    E --> F{More plans?}
    F -->|Yes| D
    F -->|No| G[/Enter user requirements and budget/]
    G --> H[Initialize eligible plans list]
    H --> I[Select a mobile plan]
    I --> J[Calculate excess data usage]
    J --> K[Calculate excess call minutes]
    K --> L[Calculate excess SMS]
    L --> M[Calculate total cost]
    M --> N{Validity sufficient?}
    N -->|No| O[Mark plan not eligible]
    N -->|Yes| P{Total cost within budget?}
    P -->|No| O
    P -->|Yes| Q[Add plan to eligible list]
    O --> R{More plans?}
    Q --> R
    R -->|Yes| I
    R -->|No| S{Eligible plans available?}
    S -->|No| T[Display no eligible plan]
    S -->|Yes| U[Find minimum total cost]
    U --> V[Display most economical plan]
    T --> W([Stop])
    V --> W
````


## 8. Result

The Python program successfully evaluates multiple telecommunications plans based on data usage, call minutes, SMS requirements, validity, and budget constraints.

It calculates excess usage charges, checks plan eligibility, compares total costs, and identifies the most economical eligible mobile plan.

Time Complexity: \\(O(n)\\), where \\(n\\) is the number of mobile plans.

Space Complexity: \\(O(n)\\), for storing mobile plan details and eligible plans.


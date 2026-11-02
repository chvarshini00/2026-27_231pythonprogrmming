# Hospital Billing and Patient Classification

## 1. Problem Statement

Develop a Python program to generate hospital bills and classify patients according to a given payment policy. The program should accept patient details, including patient ID, name, patient type, consultation charges, diagnostic charges, and treatment charges.

The program should perform the following operations:

1. Calculate consultation, diagnostic, and treatment charges.
2. Validate patient details and billing constraints.
3. Apply conditional concessions based on patient category.
4. Calculate the total bill and final payable amount.
5. Classify patients according to the payment policy.
6. Generate an itemized hospital bill displaying all charges, concessions, and payment classification.

Payment Policy:

- General patients: No concession.
- Senior citizens: 10% concession.
- Insurance patients: 15% concession.
- Below Poverty Line (BPL) patients: 25% concession.
- Maximum concession limit: ₹5,000.
- Patients with final bills above ₹20,000: High Payment Category.
- Patients with final bills between ₹5,001 and ₹20,000: Medium Payment Category.
- Patients with final bills up to ₹5,000: Low Payment Category.

## 2. Algorithm

1. Start the program.
2. Define concession rates for different patient categories.
3. Set the maximum concession limit to ₹5,000.
4. Read the patient ID and patient name.
5. Read the patient category.
6. Read consultation, diagnostic, and treatment charges.
7. Validate the patient category and ensure all charges are non-negative.
8. Calculate the total bill:

`Total Bill = Consultation + Diagnostic + Treatment`

9. Determine the concession percentage based on patient category.
10. Calculate the concession amount.
11. Apply the maximum concession limit.
12. Calculate the final payable amount:

`Final Amount = Total Bill - Concession`

13\. Classify the patient according to the final payable amount:

- Above ₹20,000: High Payment Category.
- Above ₹5,000: Medium Payment Category.
- Otherwise: Low Payment Category.

14. Display the itemized hospital bill.
15. Stop the program.



## 5. Sample Input

```
========= HOSPITAL BILLING SYSTEM =========

Enter Patient ID: P101
Enter Patient Name: Rahul
Enter Patient Type (general/senior/insurance/bpl): senior

Enter Consultation Charges: Rs. 2000
Enter Diagnostic Charges: Rs. 5000
Enter Treatment Charges: Rs. 15000
```

## 6. Sample Output

```
========== HOSPITAL INVOICE ==========

Patient ID          : P101
Patient Name        : Rahul
Patient Type        : SENIOR

--------------------------------------
Consultation Charges: Rs. 2000.0
Diagnostic Charges  : Rs. 5000.0
Treatment Charges   : Rs. 15000.0

--------------------------------------
Total Bill          : Rs. 22000.0

Concession Rate     : 10 %

Calculated Concession: Rs. 2200.0
Maximum Concession  : Rs. 5000
Final Concession    : Rs. 2200.0

--------------------------------------

Final Payable Amount: Rs. 19800.0

Patient Classification: Medium Payment Category

======================================
```

### Calculation

| Description           | Amount  |
| --------------------- | ------- |
| Consultation charges  | ₹2,000  |
| Diagnostic charges    | ₹5,000  |
| Treatment charges     | ₹15,000 |
| Total bill            | ₹22,000 |
| Concession rate       | 10%     |
| Calculated concession | ₹2,200  |
| Maximum concession    | ₹5,000  |
| Final concession      | ₹2,200  |
| Final payable amount  | ₹19,800 |

Patient Classification: Medium Payment Category because the final payable amount is between ₹5,001 and ₹20,000.

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Define concession rates and maximum limit]
    B --> C[/Enter patient ID and name/]
    C --> D[/Enter patient category/]
    D --> E{Is patient category valid?}

    E -- No --> F[Display invalid category]
    F --> Z([Stop])

    E -- Yes --> G[/Enter consultation charges/]
    G --> H[/Enter diagnostic charges/]
    H --> I[/Enter treatment charges/]

    I --> J{Are all charges non-negative?}

    J -- No --> K[Display billing error]
    K --> Z

    J -- Yes --> L[Calculate total bill]
    L --> M[Determine concession percentage]
    M --> N[Calculate concession amount]
    N --> O[Apply maximum concession limit]
    O --> P[Calculate final payable amount]

    P --> Q{Final amount above 20000?}

    Q -- Yes --> R[High Payment Category]
    Q -- No --> S{Final amount above 5000?}

    S -- Yes --> T[Medium Payment Category]
    S -- No --> U[Low Payment Category]

    R --> V[Generate hospital invoice]
    T --> V
    U --> V

    V --> W[/Display bill and classification/]
    W --> Z([Stop])
mermaid


```


## 8. Result

The Python program successfully calculates hospital consultation, diagnostic, and treatment charges, validates billing details, applies conditional concessions with a maximum limit, calculates the final payable amount, and classifies patients into High, Medium, or Low Payment Categories according to the supplied payment policy.


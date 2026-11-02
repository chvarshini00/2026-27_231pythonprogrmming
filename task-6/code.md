# Retail Billing with Multiple Discount Rules

## 1. Problem Statement

Develop a Python program to generate an itemized retail bill for multiple products purchased by a customer. The program should accept product details such as product name, category, unit price, and quantity.

The program should perform the following operations:

1. Calculate the subtotal for each product based on its price and quantity.
2. Apply category-specific tax rates.
3. Calculate discounts based on purchase amount thresholds.
4. Apply a maximum concession limit to restrict the discount.
5. Calculate the final payable amount after adding taxes and deducting discounts.
6. Display an itemized invoice containing product details, subtotal, tax, discount, and final bill amount.

## 2. Algorithm

1. Start the program.
2. Define tax rates for different product categories:
   - Electronics – 18%
   - Clothing – 5%
   - Grocery – 2%
   - Furniture – 12%
3. Set the maximum discount limit to ₹1,500.
4. Read the number of products.
5. Initialize total subtotal and total tax to zero.
6. Repeat for each product:
   - Read product name, category, unit price, and quantity.
   - Validate the product category, price, and quantity.
   - Calculate subtotal = Price × Quantity.
   - Calculate tax based on the category.
   - Add subtotal and tax to their respective totals.
   - Store product details.
7. Determine the discount rate:
   - Above ₹10,000: 15%
   - Above ₹5,000: 10%
   - Above ₹2,000: 5%
   - Otherwise: 0%.
8. Calculate the discount amount.
9. Restrict the discount to the maximum concession limit.
10. Calculate the final bill:

&#x20;  Final Bill = Total Subtotal + Total Tax − Final Discount

11. Display the itemized invoice.
12. Stop the program.


## 5. Sample Input

```
========== RETAIL BILLING SYSTEM ==========

Enter number of products: 4

Enter details of Product 1
Product name: Laptop
Category: electronics
Unit price: 50000
Quantity: 1

Enter details of Product 2
Product name: Shirt
Category: clothing
Unit price: 1000
Quantity: 2

Enter details of Product 3
Product name: Rice
Category: grocery
Unit price: 500
Quantity: 2

Enter details of Product 4
Product name: Chair
Category: furniture
Unit price: 2000
Quantity: 1
```

## 6. Sample Output

```
============== ITEMIZED INVOICE ==============

Product      Category        Price   Qty   Subtotal       Tax
-----------------------------------------------------------------
Laptop       electronics  50000.00     1   50000.00   9000.00
Shirt        clothing      1000.00     2    2000.00    100.00
Rice         grocery        500.00     2    1000.00     20.00
Chair        furniture     2000.00     1    2000.00    240.00
-----------------------------------------------------------------

Total Subtotal      : Rs. 55000.0
Total Tax           : Rs. 9360.0
Discount Rate       : 15 %
Calculated Discount : Rs. 8250.0
Maximum Discount    : Rs. 1500
Final Discount      : Rs. 1500

----------------------------------------------
FINAL PAYABLE AMOUNT: Rs. 62860.0
==============================================
```

### Calculation

| Description          | Amount  |
| -------------------- | ------- |
| Total subtotal       | ₹55,000 |
| Total tax            | ₹9,360  |
| Discount rate        | 15%     |
| Calculated discount  | ₹8,250  |
| Maximum concession   | ₹1,500  |
| Final discount       | ₹1,500  |
| Final payable amount | ₹62,860 |

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Define tax rates and maximum discount]
    B --> C[/Enter number of products/]
    C --> D[Initialize subtotal and tax]
    D --> E[/Enter product name, category, price and quantity/]
    E --> F{Is input valid?}

    F -- No --> G[Display error message]
    G --> H{More products?}

    F -- Yes --> I[Calculate product subtotal]
    I --> J[Calculate category-specific tax]
    J --> K[Add subtotal and tax to totals]
    K --> L[Store product details]
    L --> H

    H -- Yes --> E
    H -- No --> M{Check total purchase amount}

    M --> N[Determine discount percentage]
    N --> O[Calculate discount amount]
    O --> P[Apply maximum concession limit]
    P --> Q[Calculate final payable amount]

    Q --> R[Generate itemized invoice]
    R --> S[/Display product details and final bill/]
    S --> T([Stop])
mermaid



```



Result: The Python program successfully calculates product subtotals, category-specific taxes, threshold-based discounts, and maximum concession limits to generate an itemized retail invoice.

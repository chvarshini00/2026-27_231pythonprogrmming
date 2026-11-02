print("========== RETAIL BILLING SYSTEM ==========")


tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 2,
    "furniture": 12
}


MAX_DISCOUNT = 1500

n = int(input("Enter number of products: "))

products = []
total_subtotal = 0
total_tax = 0


for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Product name: ")
    category = input("Category: ").lower()
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))

   
    if category not in tax_rates:
        print("Invalid category! Product skipped.")
        continue

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity! Product skipped.")
        continue

    subtotal = price * quantity

    tax_rate = tax_rates[category]
    tax = subtotal * tax_rate / 100

    total_subtotal += subtotal
    total_tax += tax

    products.append([
        name, category, price, quantity,
        subtotal, tax, tax_rate
    ])

if total_subtotal > 10000:
    discount_rate = 15
elif total_subtotal > 5000:
    discount_rate = 10
elif total_subtotal > 2000:
    discount_rate = 5
else:
    discount_rate = 0

calculated_discount = total_subtotal * discount_rate / 100

final_discount = min(calculated_discount, MAX_DISCOUNT)

final_amount = total_subtotal + total_tax - final_discount


print("\n============== ITEMIZED INVOICE ==============")

print("{:<12} {:<13} {:>8} {:>5} {:>10} {:>9}".format(
    "Product", "Category", "Price", "Qty", "Subtotal", "Tax"
))

print("-" * 65)

for p in products:
    print("{:<12} {:<13} {:>8.2f} {:>5} {:>10.2f} {:>9.2f}".format(
        p[0], p[1], p[2], p[3], p[4], p[5]
    ))

print("-" * 65)

print("Total Subtotal      : Rs.", round(total_subtotal, 2))
print("Total Tax           : Rs.", round(total_tax, 2))
print("Discount Rate       :", discount_rate, "%")
print("Calculated Discount : Rs.", round(calculated_discount, 2))
print("Maximum Discount    : Rs.", MAX_DISCOUNT)
print("Final Discount      : Rs.", round(final_discount, 2))

print("----------------------------------------------")

print("FINAL PAYABLE AMOUNT: Rs.", round(final_amount, 2))

print("==============================================")

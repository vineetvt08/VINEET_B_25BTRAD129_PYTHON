customer_name = input("Enter customer name: ")
phone_number = input("Enter customer phone number: ")

items = []
quantities = []
prices = []

while True:
    item_name = input("\nEnter item name (or type 'done' to finish): ")
    if item_name.lower() == "done":
        break
    qty = int(input(f"Enter quantity of {item_name}: "))
    price = float(input(f"Enter unit price of {item_name}: ₹"))
    
    items.append(item_name)
    quantities.append(qty)
    prices.append(price)

print("\n" + "=" * 45)
print(f"{'PALLAVI SUPER MARKET':^45}")
print("=" * 45)
print(f"Customer Name : {customer_name}")
print(f"Phone Number  : {phone_number}")
print("-" * 45)
print(f"{'Item':<18}{'Qty':<6}{'Rate':<10}{'Total':<11}")
print("-" * 45)

subtotal = 0
for i in range(len(items)):
    item_total = quantities[i] * prices[i]
    subtotal += item_total
    print(f"{items[i]:<18}{quantities[i]:<6}{prices[i]:<10.2f}{item_total:<11.2f}")

tax_rate = 0.05
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print("-" * 45)
print(f"{'Subtotal:':<34}₹{subtotal:.2f}")
print(f"{'GST (5%):':<34}₹{tax_amount:.2f}")
print("-" * 45)
print(f"{'GRAND TOTAL:':<34}₹{grand_total:.2f}")
print("=" * 45)
print(f"{'Thank you for shopping with us!':^45}")
print("=" * 45)

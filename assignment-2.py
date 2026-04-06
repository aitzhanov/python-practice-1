store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 000 0000")

print("=" * 30)
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("=" * 30)
print()

names = []
prices = []

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.lower() == "done":
        break

    price = float(input("Enter price: "))

    names.append(product_name)
    prices.append(price)

print()
print("-" * 30)
print("Your cart (", len(names), "items):")
print("-" * 30)

for i in range(len(names)):
    print(names[i], "-", prices[i], "KZT")

print("-" * 30)

customer = input("Enter customer name: ")

subtotal = sum(prices)

if subtotal < 3000:
    discount_rate = 0
    discount_name = "No discount"
elif subtotal < 7000:
    discount_rate = 0.05
    discount_name = "Standard discount"
else:
    discount_rate = 0.15
    discount_name = "Premium discount"

discount_value = subtotal * discount_rate
total = subtotal - discount_value

receipt = {
    "customer": customer,
    "items": len(names),
    "subtotal": subtotal,
    "discount": discount_value,
    "discount_name": discount_name,
    "total": total
}

print()
print("=" * 30)
print("RECEIPT -", store_info[0])
print("=" * 30)

print("Customer :", receipt["customer"])
print("Items :", receipt["items"])
print("-" * 30)

for i in range(len(names)):
    print(names[i], "-", prices[i], "KZT")

print("-" * 30)
print("Subtotal :", receipt["subtotal"], "KZT")
print("Discount :", receipt["discount"], "KZT", "(" + receipt["discount_name"] + ")")
print("Total :", receipt["total"], "KZT")
print("=" * 30)

print()
print("Unique product tracker")

weekly_products = set()

while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    weekly_products.add(name)

print()
print("Unique products:", len(weekly_products))
print(weekly_products)
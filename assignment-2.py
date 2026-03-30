customer_name = input ("Enter customer name: ")
count = 0
sum = 0

while True:
    product_name = input ("Enter product name (or 'done' to finish): ")
    if product_name.lower () == "done":
        break
    price = float (input ("Enter price: "))
    count += 1
    sum += price

print ()
print ("Customer: ", customer_name.upper())
print ("Items : ", count)
print ("Subtotal: ", sum, "KZT")

print ()    
if (sum < 3000):
    discount = 0
    discount_name = "No discount"
elif (sum >= 3000 and sum < 7000):
    discount = 0.05
    discount_name = "5% discount"
else:
    discount = 0.15
    discount_name = "15% discount"
total_discount = sum * discount
total = sum - total_discount

print ("Discount tier: ", discount_name)
print ("Discount: ", total_discount, "KZT")
print ("Total: ", total, "KZT")

print ()
print ("Name uppercase: ", customer_name.upper())
print ("Name lowercase: ", customer_name.lower())
length = len (customer_name)
print ("Name length: ", length)
if (length > 5):
    print ("Long name")
else:
    print ("Short name")
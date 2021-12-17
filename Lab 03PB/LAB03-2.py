#Lab03-2 (ACME)

amount = float(input("Enter buying amount: "))
discount = 0.0

if amount <= 1000:
    discount = 1
elif amount > 1000 and amount < 3000:
    discount = 0.9
else:
    discount = 0.85
total = amount * discount

print("Amount due after discount is {:.2f} baht." .format(total))
#Lab04-3 Electric Store

price = 0.00
discount = 0.00

tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))
price = (6000 * tv) + (1500 * dvd) + (3000 * audio)

print("Total price is {:.2f} baht." .format(price))

if price >= 24000:
    discount = 0.20
    print("You've got a discount of {:.2f} baht." .format(price * discount))

print("Your payment is {:.2f} baht. Thank you!". format(price - (price * discount)))
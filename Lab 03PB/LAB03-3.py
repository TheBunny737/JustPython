#Lab03-3 (Car Parked Fee)

import math

hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
price = 0
total = (hours * 60) + minutes

if minutes < 0 or minutes >=60 or hours < 0:
    result = "Input Error!"
elif total <= 15:
    result = "No charge, thanks."
elif total > 15 and total <= 120:
    price = 10
    result = "Total amount due is {:d} Bahts." .format(price)
elif hours >= 2 and minutes == 0:
    price = (hours - 1) * 10
    result = "Total amount due is {:d} Bahts." .format(price)
elif hours >= 2 and minutes > 0:
    price = hours * 10
    result = "Total amount due is {:d} Bahts." .format(price)

print(result)
#Lab04-8 Assignment

minute = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

day = minute // 1440
minute -= (day * 1440)

print(">>> {:d} days before due." .format(day))

if day < 2 and minute <= 720:
    result = "I will do the assignment."
elif day >= 2 and day <= 5 and minute <= 720:
    if temp > 40 or (temp > 25 and (rain == 'Y' or rain == 'y')):
        result = "I will not do the assignment."
    else:
        result = "I will do the assignment." 
else:
    result = "I will not do the assignment."

print(result)
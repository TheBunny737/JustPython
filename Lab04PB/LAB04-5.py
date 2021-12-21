#Lab04-5 NIT

age = int(input("Enter your age: "))
income = int(input("Enter your age: "))

if age < 15 or age > 60:
    result = "Invalid age."
elif income <= 0:
    result = "Invalid income"
else:
    if income > 0 and income <= 30000:
        result = "Your negative income tax is {:.2f} Baht." .format(income * 0.2)
    else:
        result = "Your negative income tax is {:.2f} Baht." .format((80000 - income) * 0.12)

print(result)
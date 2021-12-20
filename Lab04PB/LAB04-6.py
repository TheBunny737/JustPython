#Lab04-6 (Leap Year)

year = int(input("Enter year: "))

if year < 0:
    print("Invalid year.")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("{:d} is a leap year." .format(year))
    elif year % 400 == 0:
        print("{:d} is a leap year." .format(year))
    else:
        print("{:d} is not a leap year." .format(year))
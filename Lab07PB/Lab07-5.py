#Lab07-5 (Prime Number)

devide = 0
i = 1

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("End of program, goodbye.")
        break
    elif num <= 1:
        print("Invalid input, try again.")
    else:
        while i <= num:
            if num % i == 0:
                devide += 1
            i += 1
        if devide == 2:
            print("{:d} is a prime number." .format(num))
        else:
            print("{:d} is not a prime number." .format(num))
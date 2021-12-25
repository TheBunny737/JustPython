#Lab07-7 (Prime Factor)

num = int(input("Enter positive integer: "))
i = 2

if num <= 0:
    print("Invalid number.")
elif num == 1:
    print()
else:
    while num > 1:
        if num % i == 0:
            num /= i
            print(i)
            i = 2
        else:
            i += 1
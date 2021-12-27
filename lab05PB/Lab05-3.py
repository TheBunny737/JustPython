#Lab05-3 (Count Positive Odd Number)

count = 0
while True:
    n = int(input("Enter number: "))
    if n < 0:
        break
    else:
        if n % 2 != 0:
            count += 1

print("Received {:d} odd numbers" .format(count))
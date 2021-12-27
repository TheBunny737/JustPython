#Lab05-1 (Digit Ascending)

n = int(input())
digit = 1
new_n =n
i = 0

if n <= 0:
    print("ERROR")
else:
    while digit <= n:
        new_n = n // digit % 10
        digit *= 10
        print(new_n)
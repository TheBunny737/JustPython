#Lab05-6 (Rule of 9)

n = int(input())
digit = 1
new_n =n
total = 0
i = 0

while digit <= n:
    new_n = n // digit % 10
    digit *= 10
    total += new_n
    
if total % 9 == 0:
    print("Yes", total)
else:
    print("No", total % 9)
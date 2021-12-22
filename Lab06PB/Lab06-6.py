#Lab06-6 (Digit Addition)

num = int(input())
new_num = num
reduce_num = num
total = 0
digit = 1

while reduce_num > 0:
    new_num = num // digit % 10
    reduce_num = num // digit
    total += new_num
    digit *= 10 
    if total >= 10:
        while total >= 10:
            d_digit = 1
            new_total = 0
            new_total += total // d_digit % 10
            total = total // digit
            d_digit *= 10
        total += new_total + 1

print(total)
#Lab07-8 (Count All Pythagorean)
import math

num = int(input())
a = 1
count = 0

while a <= num:
    b = 1
    while b <= a:
        if math.pow(a, 2) + math.pow(b, 2) == math.pow(num, 2):
            count += 1
        b += 1
    a += 1

print(count)
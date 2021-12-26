#Lab09-5 (Fibo)

import math

def fibo(n):
    total = (math.pow((1 + math.sqrt(5)), n) - math.pow((1 - math.sqrt(5)), n)) / (math.pow(2,n) * math.sqrt(5))
    return total

n = int(input("Enter n: "))
print("fibo({:d}) = {:.0f}" .format(n, fibo(n)))
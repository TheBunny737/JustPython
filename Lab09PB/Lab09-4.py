#Lab09-4 (Factorial)
 
def factorial(n):
    i = 1
    total = 1
    while i <= n:
        total *= i
        i += 1
    return total

n = int(input("Enter n: "))
print(str(n) + "!", '=', factorial(n))
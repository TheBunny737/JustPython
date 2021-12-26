#Lab09-1 (Prime Number Function)

def check_prime(n):
    divide = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divide += 1
        i += 1
    if divide == 2:
        return True
    else:
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
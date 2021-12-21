#Lab06-3 (GCD, LCM)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
remainder = 0
numerator = 0
denominator = 0

if n1 > n2:
    numerator = n1
    denominator = n2
else:
    numerator = n2
    denominator = n1

remainder = numerator % denominator
while remainder != 0:
    numerator = denominator
    denominator = remainder
    remainder = numerator % denominator

gcd = denominator
lcm = n1 * n2 // gcd
    
print("  >> gcd({:d}, {:d}) =     {:2d}". format(n1,n2,gcd))
print("  >> lcm({:d}, {:d}) =     {:2d}". format(n1,n2,lcm))
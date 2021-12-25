#Lab08-3 (Interest rate)

import math

def simple_interest(p, r, t):
    total = p + (p * (r / 100) * t)
    return total

def compound_interest(p, r, t):
    total = p * math.pow((1 + (r / 100)), t)
    return total

p = float(input("Enter principle: "))
q = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print("Return money for simple interest calculation is %.2f Baht." % (simple_interest(p, q, t)))
print("Return money for compound interest calculation is %.2f Baht." % (compound_interest(p, q, t)))
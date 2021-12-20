#Lab02-4 (Fraction)

print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

num = (a*d) + (b*c)
den = b*d

print("Summation of the two fractions is {:d} / {:d}" .format(num,den))
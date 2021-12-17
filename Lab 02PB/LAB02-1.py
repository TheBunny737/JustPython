#Lab02-1 (Circle Area and Circumference)

import math #Do not copy this line
r = int(input("Enter a radius: "))
radius = math.pi * math.pow(r, 2)
circumference = math.pi * 2 * r
print("Area of a circle with radius {:d} is {:.2f}" .format(r, radius))
print("Circumference of a circle with radius {:d} is {:.2f}" .format(r, circumference))
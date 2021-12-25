#Lab08-1 (Circle)
import math

def circle(r):
    circle = math.pi * math.pow(r, 2)
    return circle

def circumference(r):
    circumference = 2 * math.pi * r
    return circumference

def sphere(r):
    sphere = 4/3 * math.pi * math.pow(r, 3)
    return sphere

r = float(input("Enter a radius: "))
print("Area of a circle with radius is %.2f is %.2f." % (r, circle(r)))
print("Circumference of a circle with radius is %.2f is %.2f." % (r, circumference(r)))
print("Volume of sphere with radius is %.2f is %.2f." % (r, sphere(r)))

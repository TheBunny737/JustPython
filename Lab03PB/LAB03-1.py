#Lab03-1 (BMI)

import math

Weight = float(input("Weight (kg): "))
Height = float(input("Height (m): "))
BMI = Weight / math.pow(Height, 2)

print("BMI is {:.1f}" .format(BMI))
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal weight")
elif BMI >=25 and BMI < 30:
    print("Overweight")
else:
    print("Obesity")
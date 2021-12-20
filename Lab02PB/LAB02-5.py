#Lab02-5 (Fuel)

import math

travel = int(input())
fuel = int(input())

fuelburn = travel / 15
khaew = fuelburn / (fuel * 0.5) + 1
khwan = fuelburn / (fuel * 0.9) + 1

print("{:d}" .format(math.floor(khaew)))
print("{:d}" .format(math.floor(khwan)))
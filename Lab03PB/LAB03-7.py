#Lab03-7 (Calculate f(x))

import math
x = float(input("Enter x : "))
if x < 0:
    total = math.sqrt(math.pow(x,2) + 1)
elif x == 0:
    total = x
elif x > 0 and x <= 99:
    total = 3 * math.pow(x, 2) - math.pow(1-x, 2)
else:
    total = 2 * math.pow(x,3) - x / math.sqrt(x+1)

print("f({:.2f}) = {:d}" .format(x, math.ceil(total)))
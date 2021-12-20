#Lab02-2 (Pool)

width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))

total = (width * length * depth) * 15 
time = total / 60

print("Time to fill a pool is {:.2f} minutes." .format(time))
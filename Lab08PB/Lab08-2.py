#Lab08-2 (Digits)

def digit(n):
    n = n // 1 % 10
    return n

def tens(n):
    n = n // 10 % 10
    return n

def hundreds(n):
    n = n // 100 % 10
    return n

def thousands(n):
    n = n // 1000 % 10
    return n

def sum_degits(n):
    total = digit(n) + tens(n) + hundreds(n) + thousands(n)
    return total

# ไม่ต้อง Copy บรรทัดที่ 24 - 29
n = int(input("Enter a number (0 to 9999): "))
print("Digit place is %d." % (digit(n)))
print("Tens place is %d." % tens(n))
print("Hundreds place is %d." % (hundreds(n)))
print("Thousands place is %d." % (thousands(n)))
print("Sum of all digits is %d." % sum_degits(n))
#Lab09-6 (Alternating Sum)

# เขียนฟังก์ชันเพื่อใช้หา Alternative Sum
def alternating_sum(n):
    sum = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
        i += 1
    return sum

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}" .format(n, alternating_sum(n)))
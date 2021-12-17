#Lab01-2 (Second to Hour)

t1 = int(input("Enter your exercise time 1: "))
t2 = int(input("Enter your exercise time 2: "))
total = t1 + t2
hour = total // 3600
minute = total // 60
second = total % 60
print("It is", hour, "hours", minute, "minutes and", second, "seconds.")
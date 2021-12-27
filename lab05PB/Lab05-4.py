#Lab05-4 (Star)

n = int(input())
str = input()
i = 0

while i < n:
    j = 0
    while j <= i:
        print(str, end='')
        j += 1
    print()
    i += 1
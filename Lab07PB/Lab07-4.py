num = int(input("Enter a number: "))

i = 0
total = 1

while i <= num:
    print("{:d}! = " .format(i), end='')
    if i == 0:
        print("1 = 1")
    else:
        j = i
        while j >= 1:
            print("{:d}" .format(j), end='')
            if j != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            j -= 1
        total *= i
        print("{:d}" .format(total))
    i += 1
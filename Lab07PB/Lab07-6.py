#Lab07-6 (Double rectangle stars)

height = int(input("Enter height: "))
width = int(input("Enter width: "))
i = 0

while i < height:
    j = 0
    while j <= width:
        if i % 2 != 0:
            print(' *', end='')
        else:
            print('* ', end='')
        j += 1
    print()
    i += 1
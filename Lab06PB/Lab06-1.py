#Lab06-1 (Master mind)

target = int(input("Enter a target (4-digit integer): "))
num = int(input("Enter your guess (4-digit interger): "))
digit = 1
check_position = 0
check_digit = 0

if target == num:
    print("Congratulations, you just mastered my mind!!")
else:    
    while digit <= 1000:
        new_target = target
        new_num = num
        new_target = target // digit % 10
        new_num = num // digit % 10
        d_digit = 1
        while d_digit <= 1000:
            new2_num = num
            new2_num = num // d_digit % 10
            if new2_num == new_target:
                check_digit += 1
            d_digit *= 10
        if new_num == new_target:
            check_position += 1
            check_digit -= 1
        digit *= 10

    if check_position == 0:
        print("No positions correct", end=", ")
    elif check_position == 1:
        print("One position correct", end=", ")
    elif check_position == 2:
        print("Two positions correct", end=", ")
    elif check_position == 3:
        print("Three positions correct", end=", ")
    elif check_position == 4:
        print("Four positions correct", end=", ")
    
    if check_digit == 0:
        print("no digits correct")
    elif check_digit == 1:
        print("one digit correct")
    elif check_digit == 2:
        print("two digits correct")
    elif check_digit == 3:
        print("three digits correct")
    elif check_digit == 4:
        print("four digits correct")
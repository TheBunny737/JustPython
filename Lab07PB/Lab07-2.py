#Lab07-1 (Triangle alphabet 1)

n = int(input("Enter a number: "))
i = n

if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    while i > 0:
        j = i
        while j > 0:
            print(chr(64+j), end="")
            j -= 1
        print()
        i -= 1
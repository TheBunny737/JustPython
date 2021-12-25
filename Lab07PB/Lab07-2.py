#Lab07-2 (Triangle alphabet 2)

n = int(input("Enter a number: "))
i = n

if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    while i > 0:
        j = 0
        while j < i:
            print(chr(65+j), end="")
            j += 1
        print()
        i -= 1
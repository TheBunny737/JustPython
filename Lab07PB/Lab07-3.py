#Lab07-1 (Triangle alphabet 1)

n = int(input("Enter a number: "))

if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < n:
        j = 0
        while j <= i:
            print(chr(65+j), end="")
            j += 1
        print()
        i += 1

    i = n-1
    while i > 0:
        j = 0
        while j < i:
            print(chr(65+j), end="")
            j += 1
        print()
        i -= 1
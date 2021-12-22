#Lab07-1 (Triangle alphabet 1)

n = int(input("Enter a number: "))
i = 0

if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    while i < n:
        j = 0
        while j <= i:
            print(chr(65+j), end="")
            j += 1
        print()
        i += 1
#Lab06-2 (Guessing 3)

target = 72 # ไม่ต้อง copy บรรทัดนี้
count = 1

while True:
    num = int(input("Enter your guess: "))
    if num == target:
        print("Congratulations, your guess is correct.")
        break
    elif num < 0 or num > 100:
        print("Sorry, your guess is out of range.")
    elif num < target:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is too high.")
    count += 1

print("Total number of guesses is {:d}." .format(count))
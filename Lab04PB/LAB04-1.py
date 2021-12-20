#Lab04-1 (Guessing 2)

target = 72 #ไม่ต้อง copy บรรทัดนี้
num = int(input("Enter your guess (0 - 100): "))

if num < 0 or num > 100:
    print("Sorry, out of range, try again later.")
elif num == target:
    print("Congratulations, your guess is correct.")
elif num < target:
    print("Sorry, your guess is too low, try again later.")
else:
    print("Sorry, your guess is too high, try again later.")
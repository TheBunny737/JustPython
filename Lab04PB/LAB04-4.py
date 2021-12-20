#Lab04-4 (Buffet)

choice = input("Enter your buffet choice: ")
price = 0.00
discount = 0.00

if choice == "Korean":
    price = 1500.00
    yn = input("Is today Wednesday (yes/no)? ")
    if yn == "yes":
        discount = 0.85
    else:
        discount = 1
    print("Your payment is {:.2f} Baht." .format(price * discount))
elif choice == "Japanese":
    price = 1000.00
    yn = input("Is today Wednesday (yes/no)? ")
    if yn == "yes":
        discount = 0.85
    else:
        discount = 1
    print("Your payment is {:.2f} Baht." .format(price * discount))
else:
    print("Sorry, there is no {:s} buffet." .format(choice))
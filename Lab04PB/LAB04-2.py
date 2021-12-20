#Lab04-2 (Menu)
print("---<< Main Menu >>---")
print("   <B>urger Meal")
print("   <C>hicken Meal")
print("   <P>asta Meal")
main_menu = input("Enter your choice: ")
price = 0

if main_menu == 'B': #Burger
    print("---<< Burger Sub Menu >>---")
    print("   <R>egular Burger")
    print("   <C>heese Burger")
    print("   <D>ouble Cheese Burger")
    sub_menu = input("Enter your choice: ")
    if sub_menu == 'R':
        price = 60
        result = "Your Regular Burger is {:d} Baht." .format(price)
    elif sub_menu == 'C':
        price = 75
        result = "Your Cheese Burger is {:d} Baht." .format(price)
    elif sub_menu == 'D':
        price = 90
        result = "Your Double Cheese Burger is {:d} Baht." .format(price)
    else:
        result = "Invalid sub menu choice"

elif main_menu == 'C': #Chicken
    print("---<< Chicken Sub Menu >>---")
    print("   <F>ried Chicken")
    print("   <G>rilled Chicken")
    print("   <C>hef's Chicken")
    sub_menu = input("Enter your choice: ")
    if sub_menu == 'F':
        price = 120
        result = "Your Fried Chicken is {:d} Baht." .format(price)
    elif sub_menu == 'G':
        price = 150
        result = "Your Grilled Chicken is {:d} Baht." .format(price)
    elif sub_menu == 'C':
        price = 180
        result = "Your Chef's Chicken is {:d} Baht." .format(price)
    else:
        result = "Invalid sub menu choice"

elif main_menu == 'P': #Pasta
    print("---<< Pasta Sub Menu >>---")
    print("   <S>paghetti de Italiano")
    print("   <L>asagna Supreme")
    print("   <M>acaroni Special")
    sub_menu = input("Enter your choice: ")
    if sub_menu == 'S':
        price = 90
        result = "Your Spaghetti de Italiano is {:d} Baht." .format(price)
    elif sub_menu == 'L':
        price = 120
        result = "Your Lasagna Supreme is {:d} Baht." .format(price)
    elif sub_menu == 'M':
        price = 100
        result = "Your Macaroni Special is {:d} Baht." .format(price)
    else:
        result = "Invalid sub menu choice"

else: #Invalid
    result = "Invalid main menu choice."

print(result)
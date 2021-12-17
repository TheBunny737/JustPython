#Lab03-6 (Admin Account)

ADMIN_USERNAME = 'admin' #Do not copy this line
ADMIN_PASSWORD = 'Ad31n15Tr@t012' #Do not copy this line
Username = input("Username: ")
Password = input("Password: ")

if Username == ADMIN_USERNAME and Password == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")
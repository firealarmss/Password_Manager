#This was writen by caleb. Ham radio call ko4uyj.
#pls support  me and check out the paypal (once its actually up)

print("Thanks for using this manager.")
user = input("Please type username")
if user == ("caleb"):
    pswd = input("Please enter your password")
    if pswd == ("password"):
        print("correct")
    else:
        print("password incorect")
        exit()
else:
    print("User incorrect")
    exit()
def menu():
    print("[1] Test Passwords")
    print("[2] Input Passwords")
    print("[0} exit the program")
menu()
option = int(input("input your option here"))
if option == 1:
    with open("passwords.txt") as f:
        lines = f.readlines()
        print(lines[4])
        print(lines[3])

elif option == 2:
    print("coming soon!")

elif option == 0:
    exit()

else:
    print("Invalid answer")

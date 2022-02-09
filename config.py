#This was writen by caleb. Ham radio call ko4uyj.
#pls support  me and check out the paypal (once its actually up)

def menu():
    print("[1] Test Passwords")
    print("[2] option2") 
menu()
option = int(input("input your option here"))
if option == 1:
    f = open('passwords.txt', 'r')
    content = f.read()
    print(content)
elif option == 2:
    print("2 worked")
else:
    print("Invalid answer")
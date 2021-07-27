try:
    with open("passlist.txt", 'r') as f:
        passList = f.read()
except:
    print("Password list not found!")

userPass = input("Enter your password: ")

if userPass in passList:
    print("Your password has been found!")
else:
    print("Your password has not been found.")
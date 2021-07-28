# Trying to open the Password List
try:
    with open("passlist.txt", 'r') as f:
        passList = f.read()
        passwordList = passList.upper()

# In case an exception occurs (most probably due to the file not being found), we log it to the console
except:
    print("Password list not found!")

# Taking Input from the user and then capitalizing the input in order to disregard capitalization
userPass = input("\n\nEnter your password: ")
userPassword = userPass.upper()

# Checking if the user's password is found in the list of passwords.
if userPassword in passwordList:
    print("\n\nYour password has been found! You should consider changing it to something that is not a proper noun, a verb, or a word in the dictionary.")
else:
    print("\n\nYour password has not been found. But that does not mean that it's secure, you might be using one of the most used passwords without knowing!")

# Closing the Password List File
f.close()

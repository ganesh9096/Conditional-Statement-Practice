'''Write a program to check whether a password is valid using nested if.'''

password = input("Enter a password: ")
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print("The password is valid.")
        else:
            print("The password must contain at least one uppercase letter.")
    else:
        print("The password must contain at least one digit.")
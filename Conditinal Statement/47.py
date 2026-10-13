'''Write a program to check user role (admin, user, guest) using match case.'''

role = input("Enter Role (admin, user , guest) =  ")

match role:
    case "admin":
        print("Welcome Admin , You have a full access")
    case "user":
        print("Welcome user , You have limited access")
    case "guest":
        print("Welcome guest , You jhave only view only access")
    case _:
        print("Invalid Role")            
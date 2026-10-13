'''Write a program to print menu-based food selection using match case.'''

print ("Menu Card")
print("1 . Pizza")
print("2 . Burger")
print("3 . Sandwich")
print("4 . french fries")

choice = int(input("Enter a Choise number (1-4)"))

match choice:
    case 1:
        print("You ordered Pizza")
    case 2:
        print("Yor ordered Burger")
    case 3:
        print("You ordered Sandwich")
    case 4:
        print("You ordered French Fries")
    case _:
        print("Invalid Choise number ")

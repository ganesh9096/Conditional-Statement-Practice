'''Write a program to print result status using match case.'''

print("----- Result Status -----")
print("1. Pass")
print("2. Fail")
print("3. ATKT")

choice = int(input("Enter your result status (1-3): "))

match choice:
    case 1:
        print("Congratulations! You passed.")

    case 2:
        print("Sorry! You failed.")

    case 3:
        print("You have ATKT.")

    case _:
        print("Invalid choice!")

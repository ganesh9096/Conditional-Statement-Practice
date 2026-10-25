'''
Display menu-driven program using while loop.
'''




while True:
    print("n/-----------menu----------")
    print("1 . Addition")
    print("2 . Subtraction")
    print("3 . Multiplication")
    print("4 . Exit")

    choice = int(input("Enter your choice number = "))

    if choice == 1:
        a = int(input("Enter a first number ="))
        b = int(input("Enter a second number "))
        print("Addition of two number is = ",a + b)

    elif choice == 2:
        a = int(input("Enter a first number ="))
        b = int(input("Enter a second number ="))
        print("Subtraction of two number is =",a - b)

    elif choice == 3:
        a = int(input("Enter a first number ="))
        b = int(input("Enter a second number ="))
        print("Multiplication of two number is =",a * b)

    elif choice == 4:
        print("Program exited")
        break

    else:
        print("Invalid choice number . please Enter a valid choise number .")


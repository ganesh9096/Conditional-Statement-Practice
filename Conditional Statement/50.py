'''Write a program to build a simple ATM menu using a match case.'''


balance = 5000

print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("Your balance is:", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Money deposited successfully!")
            print("Your balance is:", balance)
        else:
            print("Invalid amount!")

    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Please collect your cash.")
            print("Your balance is:", balance)
        else:
            print("Invalid amount or insufficient balance!")

    case 4:
        print("Thank you for using our ATM!")

    case _:
        print("Invalid choice!")


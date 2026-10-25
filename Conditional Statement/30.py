'''Write a program to check the type of number (single, double, or three digit).'''
number = int(input("Enter a number: "))
if 0 <= number <= 9:
    print("The number is a single-digit number.")           
elif 10 <= number <= 99:
    print("The number is a double-digit number.")
elif 100 <= number <= 999:
    print("The number is a three-digit number.")        
else:
    print("The number is not a single, double, or three-digit number.")     
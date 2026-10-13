'''Write a program to check whether a number is a single-digit number or not.'''

num = int(input("Enter a number :"))
if num >= 0 and num <10:
    print("The number is a single-digit number")
else:
    print("The number is not a single-digit number")
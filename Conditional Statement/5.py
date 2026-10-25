'''Write a program to check whether a given year is a leap year or not.'''


year = int(input("Enter a year : "))
if year % 4 == 0:
    print("This year is a Leap year")
else:
    print("This year is not a Leap year")
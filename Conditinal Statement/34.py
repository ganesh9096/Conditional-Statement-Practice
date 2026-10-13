'''Write a program to check whether a year is a leap year and century year.'''

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year and a century year.")
        else:
            print(f"{year} is not a leap year but a century year.")
    else:
        print(f"{year} is a leap year but not a century year.")

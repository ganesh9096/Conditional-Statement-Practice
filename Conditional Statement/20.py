'''Write a program to check ticket price based on age.'''

age = int(input("Enter your age :"))
if age < 3:
    print("Ticket price is free.")
elif age >=3 and age <= 12:
    print("Ticket price is half price.")
else:
    print("Ticket price is full price.")
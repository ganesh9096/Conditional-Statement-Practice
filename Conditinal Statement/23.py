'''Write a program to calculate electricity bill based on units consumed.'''

units = float(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 5  
    print("Electricity bill =", bill)  
elif units > 100 and units <= 250:
    bill = units * 7.5
    print("Electricity bill =", bill)
else:
    bill = units * 10
    print("Electricity bill =", bill)

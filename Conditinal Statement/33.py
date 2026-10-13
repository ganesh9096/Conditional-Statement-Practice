'''Write a program to check whether a person can apply for a loan.
'''
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if income >= 5000:
    if credit_score >= 700:
        print("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan due to insufficient credit score.")
else:
    print("You are not eligible for a loan.")
'''Write a program to check whether a student is eligible for an exam (attendance +
marks).'''

attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your marks: "))      
if attendance >= 75:
    if marks >= 40:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam due to insufficient marks.")
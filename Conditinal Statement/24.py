'''Write a program to check exam results (Distinction, First Class, Pass, Fail).'''

marks = float(input("Enter your marks :"))
if marks >= 80 and marks <=100:
    print("Distinction")
elif marks >= 60 and marks < 80:
    print("First Class")
elif marks >= 40 and marks < 60:
    print("Pass")
else:
    print("Fail")
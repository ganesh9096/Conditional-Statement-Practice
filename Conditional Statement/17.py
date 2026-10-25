'''Write a program to check grade based on marks (A, B, C, Fail).'''


marks = int(input ("Enter your marks :"))
if marks >= 90 and marks <=100:
    print("A Grade")
elif marks >= 80 and marks < 90:
    print("B Grade")
elif marks >= 60 and marks < 80:
    print("C Grade")
elif marks >= 40 and marks <60:
    print("D Grade")
else:
    print("Fail")
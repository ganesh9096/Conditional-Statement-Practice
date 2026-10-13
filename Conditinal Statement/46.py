'''Write a program to print grade description using match case.'''

Grade =input("Enter a grade (O ,A ,B , C , D)").upper()

match Grade:
    case "O":
        print("Outstanding")
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Pass")
    case "D":
        print("Fail")
    case _:
        print("Invalid Grade")
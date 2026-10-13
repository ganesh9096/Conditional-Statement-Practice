'''Write a program to print language choice using match case.'''

print("Choose Language")
print("P , Python")
print("J , Java")
print("C , C")
print("JS , Javascript")

language = input("Enter a choice to select language (P, J, C, JS) = ")

match language:
    case "P":
        print("Selected language 'Python !'")
    case "J":
        print("Selected language 'Java !'")
    case "C":
        print("Selected language 'C Language!'")
    case "JS":
        print("Selected language 'Javascript !'")
    case _:
        print("Invalid choise")
    
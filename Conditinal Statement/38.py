'''Write a program to check whether a student passed all subjects.'''

# marks = []
# for i in range(1, 4):
#     mark = float(input(f"Enter marks for subject {i}: "))
#     marks.append(mark)

# if all(mark >= 40 for mark in marks):
#     print("The student has passed all subjects.")
# else:
#     print("The student has not passed all subjects.")   


Python = int(input("Enter Python marks: "))
sql = int(input("Enter sql marks: "))
Django = int(input("Enter Django marks: "))

if Python >= 35 and sql >= 35 and Django >= 35:
    print("Student Passed All Subjects")
else:
    print("Student Failed")


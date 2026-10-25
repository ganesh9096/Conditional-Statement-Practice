'''
Calculate sum of cubes of first n numbers.
'''

num = int(input("Enter a number ="))

i = 1
total = 0

while i <= num:
    cube = i * i * i
    total = cube + total
    i = i + 1

print("Sum of the cube = ",total)
'''
Calculate sum of squares of first n numbers.
'''

n = int(input("Enter a number = "))

i = 1
total = 0

while i <= n:
    square = i * i
    total = total + square
    i = i + 1

print("Sum of squares =", total)

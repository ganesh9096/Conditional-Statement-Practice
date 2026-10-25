'''
Find product of digits of a number.
'''

num = int(input("Enter a number ="))
product = 1

while (num > 0):
    digit = num % 10
    product = digit * product
    num = num // 10

print("The product of digits of number is =", product)
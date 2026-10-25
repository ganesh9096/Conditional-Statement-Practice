'''
 Find sum of numbers entered by user until 0 is entered.
'''


num = int(input("Enter the number ="))
total = 0

while (num != 0):
    total = num + total
    num = int(input("Enter the number ="))

print("Total is =", total)
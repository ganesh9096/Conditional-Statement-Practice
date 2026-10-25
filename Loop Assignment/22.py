'''
 Find sum of even digits in a number.
'''

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    # print("digit",digit)
    if digit % 2 == 0:
        total = total + digit
        # print("Total",total)
    num = num // 10
    #print("number",num)

print("Sum of even digits =", total)
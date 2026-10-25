'''
Check whether number is strong number.
'''


num = int(input("Enter a number ="))
temp = num 
total = 0


while num > 0:
    digit  = num % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i = i + 1

    total = total + fact
    num = num // 10

if (total == temp):
    print("The number is strong number.")
else:
    print("The number is not a strong number.")






'''
 Check whether a number is Armstrong.
'''

num = int(input("Enter a number = "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if num == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
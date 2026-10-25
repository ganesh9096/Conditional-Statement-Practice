'''
Check whether a string is palindrome.
'''

str = input("Enter a Word = ")
pali = ""

for ch in str:
    pali = ch + pali 
if str == pali:
    print(f"{str} is a Palindrome .")
else:
    print(f"{str} is not a palindrome")    
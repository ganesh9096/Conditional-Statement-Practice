'''
 Print alternate characters of a string.
'''

text = input("Enter a string: ")

i = 0

for ch in text:
    if i % 2 == 0:
        print(ch, end="")
    i = i + 1


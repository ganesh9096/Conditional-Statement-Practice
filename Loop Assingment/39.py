'''
Count total words in a string.
'''

char = input("Enter a sentance: ")

count = 1

for ch in char:
    if ch == " ":
        count = count + 1

print("Total words =", count)

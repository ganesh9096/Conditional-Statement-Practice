'''
Count vowels in a string.
'''


vowel = input("Enter a String =")
count = 0

for ch in vowel:
    if ch.lower() in "aeiou":
        count = count + 1
print("Vowels in a String are =", count)

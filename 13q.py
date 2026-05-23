#Write a program that accepts a sentence and calculate the number of letters and digits.
#i/p - hello world! 123    o/p - LETTERS 10  DIGITS 3


#using mehtod isalpha() and isdigit()
s = input("Enter sentence: ")

letters = 0
digits = 0

for i in s:

    if i.isalpha():
        letters += 1

    elif i.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)


#without using mehtod 
s = input("Enter sentence: ")

letters = 0
digits = 0

for i in s:

    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):

        letters += 1

    elif '0' <= i <= '9':

        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)
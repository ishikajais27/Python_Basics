#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#i/p - Hello world!    o/p - UPPER CASE 1    LOWER CASE 9
#with mehod .isupper and .islower
s = input("Enter the sentence: ")

upper = 0
lower = 0

for i in s:

    if i.isupper():

        upper += 1

    elif i.islower():

        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)

#without any method
s = input("Enter the sentence: ")

upper = 0
lower = 0

for i in s:

    if 'A' <= i <= 'Z':

        upper += 1

    elif 'a' <= i <= 'z':

        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)
#accepts sequence of str as input and prints the str after making all characters in the sentence capitalized.
#i/p -
#Hello world
#Practice makes perfect
#o/p -
#HELLO WORLD
#PRACTICE MAKES PERFECT
str = ""

while True:

    line = input()

    if line == "":
        break

    str = str + line.upper() + "\n"

print(str)
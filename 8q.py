#accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#i/p - without,hello,bag,world   o/p - bag,hello,without,world

str = input("Enter words: ").split(",")

#without method - 

for i in range(len(str)):

    for j in range(i + 1, len(str)):

        if str[i] > str[j]:

            temp = str[i]
            str[i] = str[j]
            str[j] = temp
print(str)


#with method - 
str.sort()
print(str)
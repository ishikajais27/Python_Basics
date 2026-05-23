#accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#i/p - hello world and practice makes perfect and hello world again
#o/p - again and hello makes perfect practice world
#use set container to remove duplicated data automatically and then use sorted() to sort the data.

words = input("Enter words: ").split()   #list ds
words = set(words)    #set ds
words = sorted(words)  #list again(as sorted return list)
print(words)  #o/p - ['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']
print(" ".join(words))  #Joins all words into one string.
#abc123    contains:  alphabets → abc   numbers → 123, So it is called alphanumeric
# Question asks to:
# 1. Count frequency of each word
# 2. Sort words alphanumerically
# 3. Print as word:count

# Example Input:
# New to Python or choosing between Python 2 and Python 3?

# Separate words:
# New
# to
# Python
# or
# Python
# 2
# 3?

# Count frequency:
# Python:2
# or:1


# Sort alphanumerically:  Numbers first -> Then capital letters ->  Then small letters

# Example sorted order:
# 2
# 3?
# New
# Python
# or
# to

# Note:
# 3? and 3. are different words
# Python and python are different

text = input("Enter sentence - ")

words = text.split()

print(words)
freq = {}

# Count frequency
for item in words:

    if item in freq:
        freq[item] = freq[item] + 1

    else:
        freq[item] = 1


# Sort alphanumerically
keys = list(freq.keys())

keys.sort()


# Print output
for k in keys:
    print(k + ":" + str(freq[k]))
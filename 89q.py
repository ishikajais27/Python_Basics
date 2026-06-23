# s[::2] - string[start:end:step]. Start from the beginning.Go till the end.Take every 2nd character.
# Index:  0 1 2 3 4 5 6 7 8 9
# Value:  H 1 e 2 l 3 l 4 o 5
# 0 → H
# 2 → e
# 4 → l
# 6 → l
# 8 → o

s = input()

print(s[::2])

# Without Slicing
s = input()

for i in range(0, len(s), 2):
    print(s[i], end="")
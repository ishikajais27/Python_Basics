s = input()

words = s.split()

print(" ".join(words[::-1]))

# words = s.split() -> words = ['rise', 'to', 'vote', 'sir']. converts a string into a list of words.
# words[::-1] -> ['sir', 'vote', 'to', 'rise'].
# " ".join(words[::-1]) -> sir vote to rise. joins the words back into a string with spaces.
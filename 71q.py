import random

even_numbers = list(range(0, 11, 2))

print(random.choice(even_numbers))

#range(0, 11, 2) generates: [0, 2, 4, 6, 8, 10].
# random.choice() picks one random element from that list.
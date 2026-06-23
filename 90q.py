from itertools import permutations

lst = [1, 2, 3]

for p in permutations(lst):
    print(p)
    
# A permutation means arranging elements in all possible orders.each permutation is returned as a tuple.
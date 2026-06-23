# set() converts a list into a set (removes duplicates).
# &= updates the first set with only the common elements.
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

s1 = set(list1)
s1 &= set(list2)

print(list(s1))
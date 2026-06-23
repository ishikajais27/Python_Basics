#   remove() method is a built-in list method in Python used to delete the first occurrence of a specified value from a list.
lst = [12, 24, 35, 24, 88, 120, 155]

result = [x for x in lst]
result.remove(24)

print(result)
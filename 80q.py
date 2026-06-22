# List comprehension is a short way to create a new list from an existing iterable (list, range, string, etc.).

nums = [5, 6, 77, 45, 22, 12, 24]

result = [x for x in nums if x % 2 != 0]

print(result)
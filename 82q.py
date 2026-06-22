# enumerate() is a built-in Python function that adds an index to each element of an iterable (list, tuple, string, etc.).
nums = [12, 24, 35, 70, 88, 120, 155]

result = []
for i, x in enumerate(nums):
    if i % 2 != 0:
        result.append(x)

print(result)
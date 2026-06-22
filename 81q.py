
nums = [12, 24, 35, 70, 88, 120, 155]

result = [x for x in nums if not (x % 5 == 0 and x % 7 == 0)]

print(result)
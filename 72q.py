import random

nums = [x for x in range(11) if x % 5 == 0 and x % 7 == 0]

print(random.choice(nums))
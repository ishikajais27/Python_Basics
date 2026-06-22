import random

nums = [x for x in range(1, 1001) if x % 35 == 0]

print(random.sample(nums, 5))
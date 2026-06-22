import random

nums = [3, 6, 7, 8]

random.shuffle(nums)

print(nums)

#random.shuffle() modifies the list in place and returns None. 
# def shuffle(lst):   
# #modify lst directly
# ....
# return None
num = [1,2,3,4,5,6,7,8,9,10]

# Step 1: filter even num
even = filter(lambda x: x % 2 == 0, num)

# Step 2: square those even num
squares = map(lambda x: x ** 2, even)

print(list(squares))

# i/p -  print(even)   o/p - <filter object at 0x7f9a3c1b8c40>  (object type)   this means:It is NOT a list,It is a filter iterator object ,
# It stores the rule, not the actual values
# i/p -  print(list(even))   o/p - [2, 4, 6, 8, 10]
#  i/p -  print(squares)      o/p - <map object at 0x7f9a3c1b8d00> It is a map iterator object, It waits until you use it
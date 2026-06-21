def evennum(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

for i in evennum(n):
    print(i, end=",")   
    
#yield is used in a generator function to return a value one at a time, without stopping the function completely.It saves memory.
# A generator function is a function that uses yield instead of return. 
# return  → gives everything and stops        yield   → gives one value and pauses
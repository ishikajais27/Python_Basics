num = input("enter numbers")
arr = list()
#arr.append(num)
#insert is also one method 
arr.insert(0, num)
print(arr)
#as tuple is immutable we cannot perform operations like insert,delete and update directly so we convert tuple to list perform operations and then convert back to tuple.
t = tuple(arr)
print(t)

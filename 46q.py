#map() applies a function to every element in a list.

num = [1,2,3,4,5,6,7,8,9,10]

squares = list(map(lambda x: x ** 2, num))

print(squares)
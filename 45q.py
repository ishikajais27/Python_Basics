#A lambda function = small anonymous function (without name) like arrow function in js   lambda arguments: expression
#filter() = function that selects elements from a list based on condition    filter(function, iterable)


num = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, num))

print(even)
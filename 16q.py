#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# i/p - 1,2,3,4,5,6,7,8,9       o/p - 1,3,5,7,9
num = map(int, input("Enter numbers- ").split(","))
for i in num:
    if i%2!=0:
        print(i,end=",")
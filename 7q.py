#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#i/p - 3,5     o/p - [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
X = int(input("enter row size "))
Y = int(input("enter col size "))

arr = []

for i in range(X):

    temp = []

    for j in range(Y):

        num = int(input("Enter element: "))

        temp.append(num)

    arr.append(temp)

print(arr)

# why use temp to append not directly append in arr ? -   Because arr is a 2D array we need each row to be a separate list. temp stores one complete row first.
#  we can directly append in arr but must append row lists, not single numbers.
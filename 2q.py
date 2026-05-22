# factorial of given numbers
def fact(i):
    if i==0 or i==1:
        return 1

    return i*fact(i-1)


n=int(input("Enter size"))
arr=[]

for i in range(0,n):
    arr.append(int(input("Enter number")))
    
    
for i in arr:
    print(fact(i),end=",")
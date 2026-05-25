def listSq(n):
    lists = []
    for i in range(1, n + 1):
        lists.append(i ** 2)

    print(lists)
n=int(input("Enter range - "))
listSq(n)
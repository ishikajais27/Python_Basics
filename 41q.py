def tupleSq():
    lists = []

    for i in range(1, 21):
        lists.append(i ** 2)

    tuples = tuple(lists)

    print(tuples)

tupleSq()
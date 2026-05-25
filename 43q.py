t = (1,2,3,4,5,6,7,8,9,10)

evenL = []

for i in t:
    if i % 2 == 0:
        evenL.append(i)

evenT = tuple(evenL)

print(evenT)
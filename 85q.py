lst = [12,24,35,24,88,120,155,88,120,155]

seen = set()


# if preserves set insertion order,
for x in lst:
    if x not in seen:
        seen.add(x)

print(list(seen))

#else
seen = set()
result = []

for x in lst:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)
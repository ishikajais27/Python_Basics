heads = 35
legs = 94

for r in range(heads + 1):
    c = heads - r

    if 4 * r + 2 * c == legs:
        print("r =", r)
        print("c =", c)
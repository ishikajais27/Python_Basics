try:
    n = int(input())

    if n <= 0:
        raise ValueError("n must be greater than 0")

    total = 0

    for i in range(1, n + 1):
        total += float(i) / (i + 1)

    print(round(total, 2))

except ValueError as e:
    print(e)
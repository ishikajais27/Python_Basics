nums = input().split(",")

try:
    for n in nums:
        n = int(n)
        assert n % 2 == 0

    print("All numbers are even")

except AssertionError:
    print("Not all numbers are even")
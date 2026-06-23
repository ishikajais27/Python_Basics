s = input()

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

for ch in d:
    print(ch, ",", d[ch], sep="")
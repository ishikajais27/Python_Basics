password = input("Enter password separated by comma: ").split(",")

correct = []

for p in password:

    if len(p) < 6 or len(p) > 12:
        continue

    lower = False
    upper = False
    digit = False
    special = False

    for ch in p:

        if ch >= 'a' and ch <= 'z':
            lower = True

        elif ch >= 'A' and ch <= 'Z':
            upper = True

        elif ch >= '0' and ch <= '9':
            digit = True

        elif ch in "$#@":
            special = True

    if lower and upper and digit and special:
        correct.append(p)

print(",".join(correct))
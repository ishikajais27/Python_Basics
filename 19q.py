data = []

while True:
    line = input()

    if line == "":
        break

    name, age, marks = line.split(",")

    data.append((name, int(age), int(marks)))
#data.sort()

for i in range(len(data)):
    for j in range(i + 1, len(data)):

        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print(data)


#Python compares tuples left to right automatically
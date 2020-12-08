f = open("input.txt", "r")
lines = f.read().splitlines()

for i, line in enumerate(lines):
    lines[i] = [line[:7], line[7:]]

print(lines)

highest = 0

array = []
for i in range(0, 889):
    array.append(i)

for i, line in enumerate(lines):
    minimum1 = 0
    maximum1 = 128

    minimum2 = 0
    maximum2 = 8

    for j in line[0]:
        if j == 'F':
            maximum1 -= (maximum1 - minimum1) // 2

        if j == 'B':
            minimum1 += (maximum1 - minimum1) // 2

    for j in line[1]:
        if j == 'L':
            maximum2 -= (maximum2 - minimum2) // 2

        if j == 'R':
            minimum2 += (maximum2 - minimum2) // 2

    # if ((minimum1 * 8) + minimum2) > highest:
    #     highest = ((minimum1 * 8) + minimum2)
    array.pop(array.index(((minimum1 * 8) + minimum2)))

print(array)
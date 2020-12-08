f = open("input.txt", "r")
lines = f.read().splitlines()

for i, line in enumerate(lines):
    lines[i] = line.split(' ')
    lines[i][0] = lines[i][0].split('-')
    lines[i][1] = lines[i][1].replace(':', '')

counter = 0

for i, line in enumerate(lines):
    marker = False

    if (line[1] == line[2][int(line[0][0]) - 1]) != (line[1] == line[2][int(line[0][1]) - 1]):
        counter += 1

print(counter)

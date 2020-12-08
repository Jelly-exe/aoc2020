import string

f = open("./input.txt", "r")
lines = f.read().splitlines()

temp = ''
array = []

for i, line in enumerate(lines):
    if line != '':
        temp += f'{line} '

    else:
        array.append(temp[:-1].split(' '))
        temp = ''

counter = 0

for i, items in enumerate(array):
    for j in string.ascii_lowercase:
        found = True
        for item in items:
            if item.find(j) == -1:
                found = False

        if found:
            counter += 1






print(counter)
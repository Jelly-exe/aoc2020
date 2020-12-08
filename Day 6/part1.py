import string

f = open("./input.txt", "r")
lines = f.read().splitlines()

temp = ''
array = []

for i, line in enumerate(lines):
    if line != '':
        temp += f'{line} '

    else:
        array.append(temp[:-1].replace(' ', ''))
        temp = ''

counter = 0

for i, item in enumerate(array):
    print('======')
    print(item)
    print('-------')
    for j in string.ascii_lowercase:
        print(f'{j}: {item} {item.find(j)}')
        if item.find(j) != -1:
            item = item.replace(j, '')
            counter += 1
    print('======')

print(counter)
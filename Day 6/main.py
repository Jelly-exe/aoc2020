f = open("input.txt", "r")
lines = f.read().splitlines()

string = ''

for i, line in enumerate(lines):
    if line != '':
        string += f'{line} '

    else:
        array.append([item[0] for item in [item.split(':') for item in string[:-1].split(' ')]])
        array2.append([item.split(':') for item in string[:-1].split(' ')])
        string = ''
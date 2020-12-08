f = open("input.txt", "r")
lines = f.read().splitlines()

string = ''
array = []
array2 = []

for i, line in enumerate(lines):
    if line != '':
        string += f'{line} '

    else:
        array.append([item[0] for item in [item.split(':') for item in string[:-1].split(' ')]])
        array2.append([item.split(':') for item in string[:-1].split(' ')])
        string = ''

print(array2)

values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
counter = 0

a = True
b = True
c = True
d = True
e = True
f = True
g = True

for i, line in enumerate(array):
    valid = True

    for j in values:
        if j not in line:
            valid = False
            break
        else:
            index = line.index(j)
            value = array2[i][index][1]

            if j == 'byr' and len(value) == 4 and 2002 >= int(value) >= 1920 and value.isdigit():
                a = False

            elif j == 'iyr' and len(value) == 4 and 2020 >= int(value) >= 2010 and value.isdigit():
                b = False

            elif j == 'eyr' and len(value) == 4 and 2030 >= int(value) >= 2020 and value.isdigit():
                c = False

            elif j == 'hgt' and ((value[3:] == "cm" and 193 >= int(value[:-2]) >= 150) or (value[2:] == "in" and 76 >= int(value[:-2]) >= 59)):
                d = False

            elif j == 'hcl' and len(value[1:]) == 6 and value[:1] == '#':
                e = False

            elif j == 'ecl' and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                f = False

            elif j == 'pid' and len(value) == 9 and value.isdigit():
                g = False

            else:
                valid = False

    if valid:
        counter += 1
print(f'{a} {b} {c} {d} {e} {f} {g}')
print(counter)

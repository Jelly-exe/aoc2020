f = open("input.txt", "r")
lines = f.read().splitlines()

def trees(xChange, yChange):
    x = 0
    counter = 0

    for y in range(0, len(lines), yChange):
        # z = lines[y][:x] + f'\033[91m{lines[y][x]}\033[0m' + lines[y][x + 1:]
        # print(f'({x}, {y}) - {z}')

        if lines[y][x] == '#':
            counter += 1

        x += xChange

        if x > 30:
            x -= 31

    return counter


print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))

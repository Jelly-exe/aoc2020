f = open("input.txt", "r")
lines = f.read().splitlines()

for i in lines:
    for j in lines:
        for m in lines:
            if (int(i) + int(j) + int(m)) == 2020:
                print(int(i)*int(j)*int(m))

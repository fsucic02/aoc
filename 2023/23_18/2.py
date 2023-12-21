import shoelace

input = open("23_18/input.txt").read().splitlines()
cur = [0, 0]
b = 0
seen = []
for action in input:
    direction, n = "RDLU"[int(action.split()[2][-2])], int(action.split()[2][2:-2], 16)
    b += int(n)
    if direction == 'R':
        cur[1] += int(n)
    elif direction == 'U':
        cur[0] -= int(n)
    elif direction == 'D':
        cur[0] += int(n)
    else:
        cur[1] -= int(n)

    seen.append(tuple(cur))

area = shoelace.shoelace_formula(seen)
i = area - b // 2 + 1
print(int(i + b))
input = open('23_11/input.txt').read().splitlines()
empty_r = []
for i, row in enumerate(input):
    if '#' not in row:
        empty_r.append(i)

empty_c = []
for j in range(len(input[0])):
    for i in range(len(input)):
        if input[i][j] == '#':
            break
    else:
        empty_c.append(j)

galaxies = [(i, j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == '#']

result = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        r1, r2 = galaxies[i][0], galaxies[j][0]
        c1, c2 = galaxies[i][1], galaxies[j][1]
        for r in range(min(r1, r2), max(r1, r2)):
            result += 2 if r in empty_r else 1
        for c in range(min(c1, c2), max(c1, c2)):
            result += 2 if c in empty_c else 1
    
print(result)

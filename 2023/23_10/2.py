import shoelace
input = open('23_10/input.txt').read().splitlines()

s1, s2 = None, None
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if input[i][j] == 'S':
           s1, s2 = i, j
           break 

seen = []
stack = [(s1, s2)]

stack.append((i, j))
while stack:
    i, j = stack.pop()
    if i > 0 and input[i][j] in "SJL|" and input[i-1][j] in "|7F" and (i-1, j) not in seen: # going up
        seen.append((i-1, j))
        stack.append((i-1, j))
    if j > 0 and input[i][j] in "S-J7" and input[i][j-1] in "-LF" and (i, j-1) not in seen: # going left
        seen.append((i, j-1))
        stack.append((i, j-1))
    if i < len(input) - 1 and input[i][j] in "S|7F" and input[i+1][j] in "|JL" and (i+1, j) not in seen: # going down
        seen.append((i+1, j))
        stack.append((i+1, j))
    if j < len(input[0]) - 1 and input[i][j] in "S-LF" and input[i][j+1] in "-J7" and (i, j+1) not in seen: # going right
        seen.append((i, j+1))
        stack.append((i, j+1))

# pick's theorem, shoelace formula
area = shoelace.shoelace_formula(seen)
print(area - len(seen) // 2 + 1)
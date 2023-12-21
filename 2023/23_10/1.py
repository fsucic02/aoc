input = open('23_10/input.txt').read().splitlines()

sr, sc = None, None
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if input[i][j] == 'S':
           sr, sc = i, j
           break 

seen = []
stack = []
def dfs(i, j):
    stack.append((i, j))
    while stack:
        i, j = stack.pop()
        if i > 0 and input[i][j] in "SJL|" and input[i-1][j] in "|7F" and (i-1, j) not in seen: # going up
            seen.append((i-1, j))
            stack.append((i-1, j))
        if i < len(input) - 1 and input[i][j] in "S|7F" and input[i+1][j] in "|JL" and (i+1, j) not in seen: # going down
            seen.append((i+1, j))
            stack.append((i+1, j))
        if j < len(input[0]) - 1 and input[i][j] in "S-LF" and input[i][j+1] in "-J7" and (i, j+1) not in seen: # going right
            seen.append((i, j+1))
            stack.append((i, j+1))
        if j > 0 and input[i][j] in "S-J7" and input[i][j-1] in "-LF" and (i, j-1) not in seen: # going left
            seen.append((i, j-1))
            stack.append((i, j-1))

dfs(sr, sc)
print((len(seen) + 1) // 2)
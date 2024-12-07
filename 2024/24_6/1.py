grid = [list(row) for row in open("24_6/input.txt").read().splitlines()]
i, j = next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '^')

def valid_coords(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = {
    '^': (-1, 0, '>'),
    '>': (0, 1, 'v'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^')
}

seen = set()
while True:
    if (i, j) not in seen:
        seen.add((i, j))

    direction = grid[i][j]
    di, dj, next_direction = directions[direction]
    ni, nj = i + di, j + dj

    if not valid_coords(ni, nj):
        break

    if grid[ni][nj] != '#':
        grid[i][j] = '.'
        i, j = ni, nj
        grid[i][j] = direction
    else:
        grid[i][j] = next_direction

print(len(seen))

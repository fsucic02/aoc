def valid_coords(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = {
    '^': (-1, 0, '>'),
    '>': (0, 1, 'v'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^')
}

def p1(i, j, griddy):
    path = set()
    state = set()
    while True:
        direction = griddy[i][j]
        di, dj, next_direction = directions[direction]
        ni, nj = i + di, j + dj

        if (i, j) not in path:
            path.add((i, j))

        if (i, j, direction) not in state:
            state.add((i, j, direction))
        else:
            return False

        if not valid_coords(ni, nj, griddy):
            break

        if griddy[ni][nj] != '#':
            griddy[i][j] = '.'
            i, j = ni, nj
            griddy[i][j] = direction
        else:
            griddy[i][j] = next_direction
    
    return path

grid = [list(row) for row in open("24_6/input.txt").read().splitlines()]
sr, sc = next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '^')

path = p1(sr, sc, grid)
path.remove((sr, sc))
result = 0
for (i, j) in path:
    grid_n = [list(row) for row in open("24_6/input.txt").read().splitlines()] # faster than deepcopying
    grid_n[i][j] = '#'
    if not p1(sr, sc, grid_n):
        result += 1

print(result)

grid = [list(map(int, row)) for row in open("24_10/input.txt").read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dfs(i, j):
    if grid[i][j] == 9: return 1

    result = 0    
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if valid_coords(ni, nj) and grid[ni][nj] == grid[i][j] + 1:
            result += dfs(ni, nj)

    return result

solution = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            solution += dfs(r, c)

print(solution)
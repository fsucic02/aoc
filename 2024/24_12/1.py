grid = [list(row.strip()) for row in open('24_12/input.txt').read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def n_of_neighbors(i, j):
    n = 0
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj

        if valid_coords(ni, nj) and grid[ni][nj] == grid[i][j]:
            n += 1

    return n

def dfs(i, j, visited):
    if (i, j) not in visited:
        visited.add((i, j))
        n = 4 - n_of_neighbors(i, j)
    
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if valid_coords(ni, nj) and (ni, nj) not in visited and grid[ni][nj] == grid[i][j]:
                n += dfs(ni, nj, visited)[0]
    
    return n, visited

seen, solution = set(), 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r, c) not in seen:
            n, visited = dfs(r, c, set())
            seen = seen.union(visited)
            solution += n * len(visited)
print(solution)

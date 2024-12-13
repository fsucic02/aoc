grid = [list(row.strip()) for row in open('24_12/input.txt').read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dfs(i, j, visited, horizontal, vertical):
    if (i, j) not in visited:
        visited.add((i, j))
        
        for di in [1, -1]:
            ni = i + di
            if not valid_coords(ni, j) or grid[ni][j] != grid[i][j]:
                horizontal.add((ni - 0.5 * di, j, i))
        
        for dj in [1, -1]:
            nj = j + dj
            if not valid_coords(i, nj) or grid[i][nj] != grid[i][j]:
                vertical.add((i, nj - 0.5 * dj, j))

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if valid_coords(ni, nj) and (ni, nj) not in visited and grid[ni][nj] == grid[i][j]:
                dfs(ni, nj, visited, horizontal, vertical)
    
    return visited, horizontal, vertical

solution, seen = 0, set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if (r, c) not in seen:
            visited, horizontal, vertical = dfs(r, c, set(), set(), set())
            seen = seen.union(visited)
            
            vertical_diff = set()
            for edge in vertical:
                i, nj, j = edge
                if (i + 1, nj, j) in vertical:
                    vertical_diff.add(edge)
            vertical -= vertical_diff

            horizontal_diff = set()
            for edge in horizontal:
                ni, j, i = edge
                if (ni, j + 1, i) in horizontal:
                    horizontal_diff.add(edge)
            horizontal -= horizontal_diff

            solution += len(visited) * (len(vertical) + len(horizontal))

print(solution)
    
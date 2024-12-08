from itertools import combinations

grid = [list(row) for row in open("24_8/input.txt").read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

solution = set()
seen = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j].isalnum() and grid[i][j] not in seen:
            seen.add(grid[i][j])

            coords = [
                (r, c)
                for r in range(len(grid))
                for c in range(len(grid[0]))
                if grid[r][c] == grid[i][j]
            ]

            pairs = list(combinations(coords, 2))
            for p1, p2 in pairs:
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                for antinode in [(p1[0] - dx, p1[1] - dy), (p2[0] + dx, p2[1] + dy)]:
                    if valid_coords(*antinode):
                        solution.add(antinode)
                    
print(len(solution))

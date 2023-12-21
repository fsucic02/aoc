input = open("23_21/input.txt").read().splitlines()

sr, sc = [(i, j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == "S"][0]

queue = [(sr, sc, 6)]
seen = {(sr, sc)}
ans = set()
while queue:
    i, j, n = queue.pop(0)
    if n % 2 == 0:
        ans.add((i, j))
    if n == 0:
        continue
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ii, jj = i + dx, j + dy
        if ii < 0 or ii >= len(input) or jj < 0 or jj >= len(input[0]) or (ii, jj) in seen or input[ii][jj] == "#":
            continue
        queue.append((ii, jj, n - 1))
        seen.add((ii, jj))

print(len(ans))
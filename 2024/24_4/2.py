data = [list(row) for row in open("24_4/input.txt").read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])

def x_mas(row, col):
    if not valid_coords(row - 1, col - 1): return 0
    if not valid_coords(row + 1, col + 1): return 0
    if not valid_coords(row - 1, col + 1): return 0
    if not valid_coords(row + 1, col - 1): return 0

    return set([data[i - 1][j - 1], data[i + 1][j + 1]]) == {'M', 'S'} and set([data[i - 1][j + 1], data[i + 1][j - 1]]) == {'M', 'S'}

result = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'A':
            result += x_mas(i, j)
            
print(result)
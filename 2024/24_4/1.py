data = [list(row) for row in open("24_4/input.txt").read().splitlines()]

def valid_coords(i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])

def check_vertical(row, col, direction):
    if not valid_coords(row + 3 * direction, col): return 0 

    return ''.join(data[row + k * direction][col] for k in range(1, 4)) == "MAS"

def check_horizontal(row, col, direction):
    if not valid_coords(row, col + 3 * direction): return 0 

    return ''.join(data[row][col + k * direction] for k in range(1, 4)) == "MAS"

def check_main_diagonal(row, col, direction):
    if not valid_coords(row + 3 * direction, col + 3 * direction): return 0 

    return ''.join(data[row + k * direction][col + k * direction] for k in range(1, 4)) == "MAS"

def check_secondary_diagonal(row, col, direction):
    if not valid_coords(row + 3 * direction, col - 3 * direction): return 0 

    return ''.join(data[row + k * direction][col - k * direction] for k in range(1, 4)) == "MAS"

result = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'X':
            result += sum(
                check_func(i, j, direction)
                for check_func in [check_vertical, check_horizontal, check_main_diagonal, check_secondary_diagonal]
                for direction in [1, -1]
            )

            
print(result)
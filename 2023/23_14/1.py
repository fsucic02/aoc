data = open("23_14/input.txt").read().splitlines()

copy = [list(row) for row in data]

for i in range(1, len(copy)):
    for j in range(len(copy[0])):
        if copy[i][j] == 'O':
            if copy[i-1][j] != '.':
                continue
            for k in range(i - 1, -1, -1):
                if copy[k][j] != '.':
                    copy[k+1][j] = 'O'
                    copy[i][j] = '.'
                    break
            else:
                copy[0][j] = 'O'
                copy[i][j] = '.'

result = 0
for i in range(0, len(copy)):
    for j in range(len(copy[0])):
        if copy[i][j] == 'O':
            result += len(copy) - i

print(result)
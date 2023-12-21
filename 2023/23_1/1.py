result = 0
with open('23_1/puzzle.txt') as f:
    for line in f:
        line = list(filter(lambda c: c.isnumeric(), line))
        result += int(line[0]) * 10 + int(line[-1])

print(result) 

import re

sum = 0
with open('23_2/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        patterns = [re.compile(fr'(\d+)\s+{color}') for color in ['red', 'green', 'blue']]
        matches = [[int(char) for char in pattern.findall(line)] for pattern in patterns]
        if max(matches[0]) > 12 or max(matches[1]) > 13 or max(matches[2]) > 14:
            pass
        else:
            sum += int(re.compile(r'Game (\d+):').findall(line)[0])

print(sum)
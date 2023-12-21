import re

sum = 0
with open('23_2/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        patterns = [re.compile(fr'(\d+)\s+{color}') for color in ['red', 'green', 'blue']]
        matches = [[int(char) for char in pattern.findall(line)] for pattern in patterns]
        sum += max(matches[0]) * max(matches[1]) * max(matches[2])

print(sum)
import re
from math import prod

data = open('24_14/input.txt').read().splitlines()
h, w = 103, 101

robots = []
for robot in data:
    robot = list(map(int, re.findall(r'(-?\d+)', robot)))
    p, v = robot[:2], robot[2:]

    p[0] = (p[0] + 100 * v[0]) % w
    p[1] = (p[1] + 100 * v[1]) % h
    
    robots.append((p, v))

quadrants = [
    [0, 0],
    [0, 0]
]
for robot in robots:
    p1, p2 = robot[0]
    if p1 == w // 2 or p2 == h // 2: continue

    quadrants[int(p1 // (w/ 2))][int(p2 // (h / 2))] += 1
    
print(prod(sum(quadrants, [])))

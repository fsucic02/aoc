import re

data = open('24_14/input.txt').read().splitlines()
h, w = 103, 101

robots = []
for robot in data:
    robot = list(map(int, re.findall(r'(-?\d+)', robot)))
    p, v = robot[:2], robot[2:]
    
    robots.append((p, v))

for second in range(1, 10_000):
    seen = set()
    for i, robot in enumerate(robots):
        p, v = robot
        p[0] = (p[0] + v[0]) % w
        p[1] = (p[1] + v[1]) % h
        seen.add(tuple(p))
    
    if len(seen) == len(data):
        break

print(second)

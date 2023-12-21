import math
from functools import reduce

data = open('23_8/input.txt').read().split('\n')

instructions, nodes = data[0], data[2:]
lookup, curr = {}, []
for node in nodes:
    first, next = node.split('=')[0].strip(), node.split('=')[1].strip()
    left, right = next.split(',')[0][1::], next.split(',')[1][:-1].lstrip()
    lookup[first] = (left, right)
    if first.endswith('A'):
        curr.append(first)

results = []
for node in curr:
    results.append(0)
    while not node.endswith('Z'):
        for instruction in instructions:
            if instruction == 'L':
                node = lookup[node][0]
            else:
                node = lookup[node][1]
            results[-1] += 1
            
print(math.lcm(*results))
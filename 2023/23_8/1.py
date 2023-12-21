data = open('23_8/input.txt', 'r').read().split('\n')

instructions, nodes = data[0], data[2:]
lookup, curr = {}, 'AAA'

for node in nodes:
    first, next = node.split('=')[0].strip(), node.split('=')[1].strip()
    left, right = next.split(',')[0][1::], next.split(',')[1][:-1:].lstrip()
    lookup[first] = (left, right)
    
result = 0
while (curr != 'ZZZ'):
    for instruction in instructions:
        if instruction == 'L':
            curr = lookup[curr][0]
        else:
            curr = lookup[curr][1]

        result += 1

print(result)
data = open('24_9/input.txt').read()

map = []
block = 0
for cnt, i in enumerate(data):
    for _ in range(int(i)):
        map.append(block if cnt % 2 == 0 else '.')
    if cnt % 2 == 0: block += 1

left, right = 0, len(map) - 1
while left < right - 1:
    if map[left] != '.': 
        left += 1
        continue

    if map[right] == '.':
        right -= 1
        continue

    map[left]  = map[right]
    map[right] = '.'

print(sum([c * idx for idx, c in enumerate(list(filter(lambda c: c != '.', map)))]))

data = open('24_9/input.txt').read()

map, block = [], 0
for cnt, i in enumerate(data):
    for _ in range(int(i)):
        map.append(block if cnt % 2 == 0 else '.')
    if cnt % 2 == 0: block += 1

def find_dot_groups(map):
    dot_groups, i = [], 0
    while i < len(map):
        if map[i] == '.':
            start = i
            while i < len(map) and map[i] == '.':
                i += 1
            length = i - start
            dot_groups.append((start, length))

        else:
            i += 1

    return dot_groups

dot_groups = find_dot_groups(map)
curr, right = map[-1], len(map) - 1
while curr >= 1:    
    num_cnt = map.count(curr)
    if num_cnt == 0: curr -= 1

    num_idx = map.index(curr)

    group = next((group for group in list(filter(lambda group : group[0] < num_idx, dot_groups)) if group[1] >= num_cnt), None)
    if not group:
        curr -= 1
        continue
    
    group_idx = dot_groups.index(group)
    if group[1] - num_cnt == 0:
        dot_groups.pop(group_idx)
    else:
        dot_groups[group_idx] = (group[0] + num_cnt, group[1] - num_cnt)

    map[group[0]:group[0] + num_cnt] = [curr] * num_cnt
    map[num_idx:num_idx + num_cnt] = ['.'] * num_cnt
    curr -= 1

print(sum([c * idx for idx, c in enumerate(map) if map[idx] != '.']))

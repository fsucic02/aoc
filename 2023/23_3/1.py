def is_adjacent(coordinates, symbol):
    x1, y1 = coordinates
    x2, y2 = symbol

    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

result = 0
with open('23_3/input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])
nums = {}
symbols = []
i = 0
while i < rows:
    j = 0
    while j < cols:
        if lines[i][j].isdigit():
            k = j + 1
            num = lines[i][j]
            while k < cols and lines[i][k].isdigit():
                num += lines[i][k]
                k += 1
            
            if not nums.get(int(num), []):
                nums[int(num)] = []
            nums[int(num)].append([])
            for l in range(len(num)):
                nums[int(num)][-1].append((i, l + j))
            j = k
        else:
            if lines[i][j] != '.':
                symbols.append((i, j))
            j += 1

    
    i += 1

for num in nums:
    for set_of_cords in nums[num]:
        flag = False
        for coordinates in set_of_cords:
            for symbol in symbols:
                if is_adjacent(coordinates, symbol):
                    flag = True
                    result += num
                    break
            if flag == True:
                break

print(result)
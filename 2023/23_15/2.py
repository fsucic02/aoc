data = open("23_15/input.txt").read().split(",")

def get_hash(string):
    curr = 0
    for char in string:
        curr += ord(char)
        curr *= 17
        curr %= 256
    
    return curr

boxes = [[] for _ in range(256)]
for action in data:
    hashed = get_hash(action.split("=" if "=" in action else "-")[0])
    if "=" in action:
        for i, tup in enumerate(boxes[hashed]):
            if tup[0] == action.split("=")[0]:
                boxes[hashed][i] = tuple(action.split("="))
                break
        else:
            boxes[hashed].append(tuple(action.split("=")))
    else:
        # - in action
        for tup in boxes[hashed]:
            if tup[0] == action.split("-")[0]:
                boxes[hashed].remove(tup)
result = 0
for i, box in enumerate(boxes, 1):
    for j, seq in enumerate(box, 1):
        result += i * j * int(box[j-1][1])

print(result)
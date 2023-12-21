data = open("23_15/input.txt").read().split(",")

result = 0
for string in data:
    curr = 0
    for char in string:
        curr += ord(char)
        curr *= 17
        curr %= 256
    
    print(curr)
    result += curr

print(result)
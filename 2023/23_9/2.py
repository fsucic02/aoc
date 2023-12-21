data = open('23_9/input.txt').read().split('\n')
data = [[int(num) for num in l.split()] for l in data]

i, result = 0, 0
while i < len(data):
    diffs_array = []
    history = data[i]
    diffs_array.append(history)
    diffs = [history[i+1] - history[i] for i in range(len(history) - 1)]
    addend = [diffs[-1]]
    diffs_array.append(diffs)
    while (not all(x == 0 for x in diffs)):
        history = diffs
        diffs = [history[i+1] - history[i] for i in range(len(history) - 1)]
        diffs_array.append(diffs)
    i += 1

    temp = 0
    for array in diffs_array[-2:-len(diffs_array):-1]:
        temp = array[0] - temp
    else:
        result += diffs_array[0][0] - temp

print(result)
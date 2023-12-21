data = open('23_9/input.txt').read().split('\n')
data = [[int(num) for num in l.split()] for l in data]

i, result = 0, 0
while i < len(data):
    history = data[i]
    result += history[-1]
    diffs = [history[i+1] - history[i] for i in range(len(history) - 1)]
    addend = [diffs[-1]]
    while (not all(x == 0 for x in diffs)):
        history = diffs
        diffs = [history[i+1] - history[i] for i in range(len(history) - 1)]
        addend.append(diffs[-1])

    result += sum(addend)
    i += 1

print(result)
words = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e' 
        }

sum = 0
with open('23_1/puzzle.txt') as f: 
    for line in f:
        for word in words:
            line = line.replace(word, f'{words[word]}')
        line = list(filter(lambda c: c.isnumeric(), line))
        sum += int(line[0]) * 10 + int(line[-1])

print(sum)
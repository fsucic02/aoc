data = open('24_2/input.txt').read().splitlines()

result = 0

for row in data:
    report = list(map(int, row.split()))
    diffs  = [report[i] - report[i+1] for i in range(len(report) - 1)]

    if all(0 < x < 4 for x in diffs) or all(-4 < x < 0 for x in diffs):
        result += 1

print(result)

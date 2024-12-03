data = open('24_2/input.txt').read().splitlines()

result = 0

def is_safe(report):
    diffs = [report[i] - report[i+1] for i in range(len(report) - 1)]
    return all(0 < x < 4 for x in diffs) or all(-4 < x < 0 for x in diffs)

for row in data:
    report = list(map(int, row.split()))
    
    if is_safe(report):
        result += 1
        continue

    for idx in range(len(report)):
        report_new = report.copy()
        report_new.pop(idx)

        if is_safe(report_new):
            result += 1
            break

print(result)

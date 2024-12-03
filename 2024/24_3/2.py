import re

data = open('24_3/input.txt').read()
data = re.sub(r"don't\(\).*?do\(\)", '', data, flags=re.DOTALL)

pattern = re.compile(r'mul\((\d+),(\d+)\)')

result = 0
for match in pattern.findall(data):
    n1, n2 = tuple(map(int, match))
    result += n1 * n2

print(result)

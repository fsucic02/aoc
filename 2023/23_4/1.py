import re

result = 0
with open('23_4/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        pattern = re.compile(r'Card\s+(\d+):\s*((\d+\s*)+)\|(\s*(\d+\s*)+)')
        match = pattern.match(line)
        card_id = match.group(1)
        winning_numbers = set(re.findall(r'\d+', match.group(2)))
        my_numbers = set(re.findall(r'\d+', match.group(4)))
        intersection = winning_numbers & my_numbers
        result += 2**(len(intersection) - 1) if intersection else 0

print(result)

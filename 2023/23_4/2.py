import re

result = 0
wins = {}
matches = {}
with open('23_4/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        pattern = re.compile(r'Card\s+(\d+):\s*((\d+\s*)+)\|(\s*(\d+\s*)+)')
        match = pattern.match(line)
        card_id = int(match.group(1))
        winning_numbers = set(re.findall(r'\d+', match.group(2)))
        my_numbers = set(re.findall(r'\d+', match.group(4)))
        intersection = winning_numbers & my_numbers
        if not wins.get(card_id, []):
            wins[card_id] = len(intersection)
        matches[card_id] = matches.get(card_id, 0) + 1
        for j in range(len(intersection)):
            matches[card_id + j + 1] = matches.get(card_id + j + 1, 0) + matches[card_id]

result = sum(wins[id] * matches[id] + 1 for id in wins)
print(result)
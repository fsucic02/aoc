import re
import functools

rules, pages = open('24_5/input.txt').read().split('\n\n')

ref = {}
pattern = r'^(\d+)\|(\d+)$'
for rule in rules.splitlines():
    match = re.match(pattern, rule.strip()).groups()
    key, val = map(int, match)
    ref[key] = ref.get(key, []) + [val]

def my_cmp(a, b):
    if b not in ref.get(a, []):
        return 1
    else:
        return -1

result = 0
for page in pages.splitlines():
    page = list(map(int, page.split(',')))
    if page == sorted(page, key=functools.cmp_to_key(my_cmp)):
        result += page[(len(page) - 1) // 2]

print(result)
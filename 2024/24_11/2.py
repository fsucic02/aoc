from functools import lru_cache

data = list(map(int, open('24_11/input.txt').read().split()))

@lru_cache(maxsize=None)
def length(n, blinks_n):
    if blinks_n == 0:
        return 1

    if n == 0:
        return length(1, blinks_n - 1)
    
    if (l := len(str(n))) % 2 == 0:
        return length(int(str(n)[:l // 2]), blinks_n - 1) + length(int(str(n)[l // 2:]), blinks_n - 1)
    else:
        return length(n * 2024, blinks_n - 1)

print(sum([length(n, 75) for n in data]))
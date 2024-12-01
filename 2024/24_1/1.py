data = open('24_1/input.txt').read().splitlines()

ll, rl = [], []
for pair in data:
    n1, n2 = map(int, pair.split())
    ll.append(n1)
    rl.append(n2)

ll.sort()
rl.sort()

print(sum(abs(l - r) for l, r in zip(ll, rl)))

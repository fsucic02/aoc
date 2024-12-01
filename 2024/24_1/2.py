data = open('24_1/input.txt').read().splitlines()

ll, rl = [], []
for pair in data:
    n1, n2 = map(int, pair.split())
    ll.append(n1)
    rl.append(n2)

ref = {}
result = 0
for num in ll:
    if num in ref.keys():
        result += ref[num]
        continue
    
    result += num * rl.count(num)
    ref[num] = result

print(result)

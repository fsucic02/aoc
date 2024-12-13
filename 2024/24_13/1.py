import re

data = open('24_13/input.txt').read().split('\n\n')

def solve(x_a, y_a, x_b, y_b, x_sol, y_sol):
    min_cost = 0

    for n_a in range(101):
        for n_b in range(101):
            if n_a * x_a + n_b * x_b == x_sol and n_a * y_a + n_b * y_b == y_sol:
                if (cost := 3 * n_a + n_b) < min_cost or min_cost == 0:
                    min_cost = cost
                    
    return min_cost

answer = 0
for claw in data:
    answer += solve(*list(map(int, re.findall(r'(\d+)', claw))))
print(answer)
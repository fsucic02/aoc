import re

data = [claw.split('\n') for claw in open('24_13/input.txt').read().split('\n\n')]

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
    button_a = list(map(int, re.findall(r'\d+', claw[0])))
    button_b = list(map(int, re.findall(r'\d+', claw[1])))
    solution = list(map(int, re.findall(r'\d+', claw[2])))
    answer += solve(button_a[0], button_a[1], button_b[0], button_b[1], solution[0], solution[1])
print(answer)
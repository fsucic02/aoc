import re

data = [claw.split('\n') for claw in open('24_13/input.txt').read().split('\n\n')]

def solve(x_a, y_a, x_b, y_b, x_sol, y_sol):
    # n_a * x_a + n_b * x_b = x_sol
    # n_a * y_a + n_b + y_b = y_sol

    D  = x_a * y_b - x_b * y_a
    
    if D == 0: return 0

    D_n_a = x_sol * y_b - x_b * y_sol
    D_n_b = x_a * y_sol - x_sol * y_a

    if D_n_a % D != 0 or D_n_b % D != 0: return 0

    n_a, n_b = round(D_n_a / D), round(D_n_b / D)

    return 3 * n_a + n_b

answer = 0
for claw in data:
    button_a = list(map(int, re.findall(r'\d+', claw[0])))
    button_b = list(map(int, re.findall(r'\d+', claw[1])))
    solution = list(map(lambda n : int(n) + 10_000_000_000_000, re.findall(r'\d+', claw[2])))
    answer += solve(button_a[0], button_a[1], button_b[0], button_b[1], solution[0], solution[1])

print(answer)
import re

data = open('24_13/input.txt').read().split('\n\n')

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
    x_a, y_a, x_b, y_b, x_sol, y_sol = list(map(int, re.findall(r'(\d+)', claw)))
    x_sol, y_sol = x_sol + 10_000_000_000_000, y_sol + 10_000_000_000_000
    answer += solve(x_a, y_a, x_b, y_b, x_sol, y_sol)

print(answer)
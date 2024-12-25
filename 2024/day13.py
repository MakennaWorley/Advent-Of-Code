# day 13
import re

def min_cost_claw(a_x, a_y, b_x, b_y, p_x, p_y):
    INF = float('inf')

    dynamic_programming = [[INF] * (p_y + 1) for _ in range(p_x + 1)]
    dynamic_programming[0][0] = 0

    for x in range(p_x + 1):
        for y in range(p_y + 1):
            if dynamic_programming[x][y] == INF:
                continue

            if x + a_x <= p_x and y + a_y <= p_y:
                dynamic_programming[x + a_x][y + a_y] = min(
                    dynamic_programming[x + a_x][y + a_y],
                    dynamic_programming[x][y] + 3
                )

            if x + b_x <= p_x and y + b_y <= p_y:
                dynamic_programming[x + b_x][y + b_y] = min(
                    dynamic_programming[x + b_x][y + b_y],
                    dynamic_programming[x][y] + 1
                )

    return dynamic_programming[p_x][p_y] if dynamic_programming[p_x][p_y] != INF else None


def min_cost_claw_large(a_x, a_y, b_x, b_y, p_x, p_y):
    delta = a_x * b_y - a_y * b_x
    if delta == 0:
        return None

    delta_a = p_x * b_y - p_y * b_x
    delta_b = a_x * p_y - a_y * p_x

    if delta_a % delta != 0 or delta_b % delta != 0:
        return None

    n_a = delta_a // delta
    n_b = delta_b // delta

    if n_a < 0 or n_b < 0:
        return None

    if n_a * a_x + n_b * b_x != p_x or n_a * a_y + n_b * b_y != p_y:
        return None

    cost = int(n_a) * 3 + int(n_b) * 1
    return cost


count = 0
count2 = 0
text = open('inputs/day13_input.txt').read().strip()

pattern = r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)"
matches = re.findall(pattern, text)

parsed_results = [
    (int(a_x), int(a_y), int(b_x), int(b_y), int(p_x), int(p_y))
    for a_x, a_y, b_x, b_y, p_x, p_y in matches
]

for a_x, a_y, b_x, b_y, p_x, p_y in parsed_results:
    cost = min_cost_claw(a_x, a_y, b_x, b_y, p_x, p_y)
    if cost is not None:
        count += cost

for a_x, a_y, b_x, b_y, p_x, p_y in parsed_results:
    cost = min_cost_claw_large(a_x, a_y, b_x, b_y, p_x+10000000000000, p_y+10000000000000)
    if cost is not None:
        count2 += cost

print(count)
print(count2)
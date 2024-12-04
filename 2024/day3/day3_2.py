# day 3: puzzle 2
import re

total = 0
process = True

file = open('2024/day3/day3_input.txt', 'r')
data = file.read()
file.close()

for expr in re.findall(r"(don\'t\(\)|do\(\)|mul\(\d+,\d+\))", data):
    if expr == "don't()":
        process = False
    elif expr == "do()":
        process = True
    elif process:
        L, R = re.findall(r"\d+", expr)
        total += int(L) * int(R)

print(total)
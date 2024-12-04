# day 3: puzzle 1
import re

total = 0

file = open('2024/day3/day3_input.txt', 'r')
data = file.read()
file.close()

for expr in re.findall(r"mul\(\d+,\d+\)", data):
    L, R = re.findall(r"\d+", expr)
    total += int(L) * int(R)

print(total)
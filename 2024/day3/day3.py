# day 3
import re

total = 0
total2 = 0
process = True

file = open('day3_input.txt', 'r')
data = file.read()
file.close()

for expr in re.findall(r"mul\(\d+,\d+\)", data):
    L, R = re.findall(r"\d+", expr)
    total += int(L) * int(R)

for expr in re.findall(r"(don\'t\(\)|do\(\)|mul\(\d+,\d+\))", data):
    if expr == "don't()":
        process = False
    elif expr == "do()":
        process = True
    elif process:
        L, R = re.findall(r"\d+", expr)
        total2 += int(L) * int(R)

print(total)
print(total2)
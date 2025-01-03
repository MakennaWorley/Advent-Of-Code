# day 3
import re

count = 0
count2 = 0
process = True

file = open('inputs/day3_input.txt', 'r')
data = file.read()
file.close()

for expr in re.findall(r"mul\(\d+,\d+\)", data):
    L, R = re.findall(r"\d+", expr)
    count += int(L) * int(R)

for expr in re.findall(r"(don\'t\(\)|do\(\)|mul\(\d+,\d+\))", data):
    if expr == "don't()":
        process = False
    elif expr == "do()":
        process = True
    elif process:
        L, R = re.findall(r"\d+", expr)
        count2 += int(L) * int(R)

print(count)
print(count2)
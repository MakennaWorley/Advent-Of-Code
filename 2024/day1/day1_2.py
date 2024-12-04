# day 1: puzzle 2
from collections import Counter

list_1 = []
list_2 = []
similarity = 0

with open('2024/day1/day1_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            list_1.append(int(parts[0]))
            list_2.append(int(parts[1]))

    file.close()

list_2_dict = dict(Counter(list_2))

for i in range(len(list_1)):
    value = list_1[i]
    similarity += (list_2_dict.get(value, 0) * value)

print(similarity)
# day 1
from collections import Counter

list_1 = []
list_2 = []
count = 0
count2 = 0

with open('inputs/day1_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            list_1.append(int(parts[0]))
            list_2.append(int(parts[1]))

    file.close()

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

list_2_dict = dict(Counter(list_2))

if len(sorted_list_1) == len(sorted_list_2):
    for i in range(len(sorted_list_1)):
        count += abs(sorted_list_1[i] - sorted_list_2[i])

for i in range(len(list_1)):
    value = list_1[i]
    count2 += (list_2_dict.get(value, 0) * value)

print(count)
print(count2)
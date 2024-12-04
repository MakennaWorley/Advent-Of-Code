# day 1: puzzle 1
list_1 = []
list_2 = []
difference = 0

with open('2024/day1/day1_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            list_1.append(int(parts[0]))
            list_2.append(int(parts[1]))

    file.close()

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

if len(sorted_list_1) == len(sorted_list_2):
    for i in range(len(sorted_list_1)):
        difference += abs(sorted_list_1[i] - sorted_list_2[i])

print(difference)
# day 5
count = 0
count2 = 0
instructions = {}
reversed_instructions = {}

text = open('inputs/day5_input.txt').read().strip()
page_order, updates = text.split('\n\n')

for line in page_order.split('\n'):
    first_page, second_page = line.split('|')
    first_page, second_page = int(first_page), int(second_page)

    if second_page not in instructions:
        instructions[second_page] = set()
    if first_page not in reversed_instructions:
        reversed_instructions[first_page] = set()

    instructions[second_page].add(first_page)
    reversed_instructions[first_page].add(second_page)

for page in updates.split('\n'):
    list = [int(first_page) for first_page in page.split(',')]

    if len(list)%2 != 1:
        break

    ok = True
    for i,first_page in enumerate(list):
        for j,second_page in enumerate(list):
            if i < j and second_page in instructions.get(first_page, set()):
                ok = False
    if ok:
        count += list[len(list)//2]
    else:
        good = []
        queue = []
        dict = {item: len(instructions.get(item, set()) & set(list)) for item in list}
        for item in list:
            if dict[item] == 0:
                queue.append(item)
        while queue:
            x = queue.pop(0)
            good.append(x)
            for y in reversed_instructions.get(x, set()):
                if y in dict:
                    dict[y] -= 1
                    if dict[y] == 0:
                        queue.append(y)
        count2 += good[len(good) // 2]

print(count)
print(count2)
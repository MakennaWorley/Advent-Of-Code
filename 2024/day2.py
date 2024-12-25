# day 2
def is_report_count(head, tail, sign):
    if not tail:
        return True

    new_head = int(tail.pop(0))

    if sign is None:
        if new_head < head:
            sign = 'negative'
        elif new_head > head:
            sign = 'positive'
        else:
            return False

    match sign:
        case 'positive':
            if (head + 3) >= new_head >= (head + 1):
                return is_report_count(new_head, tail, sign)
            else:
                return False
        case 'negative':
            if (head - 3) <= new_head <= (head - 1):
                return is_report_count(new_head, tail, sign)
            else:
                return False


def is_removed_report_count(line):
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]

        head = modified_line[0]
        tail = modified_line[1:]

        if is_report_count(head, tail, None):
            return True
    return False


count = 0
count2 = 0

with open('inputs/day2_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        parts = [int(x) for x in parts]

        head = parts.pop(0)
        tail = parts
        sign = None

        if is_report_count(head, tail, sign):
            count += 1

    file.close()

with open('inputs/day2_input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        parts = [int(x) for x in parts]

        parts_2 = parts.copy()

        head = int(parts.pop(0))
        tail = parts
        sign = None

        if is_report_count(head, tail, sign) or is_removed_report_count(parts_2):
            count2 += 1
    file.close()

print(count)
print(count2)
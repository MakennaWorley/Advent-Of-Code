# day 2: puzzle 1
safe = 0

def is_report_safe(head, tail, sign):
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
                return is_report_safe(new_head, tail, sign)
            else:
                return False
        case 'negative':
            if (head - 3) <= new_head <= (head - 1):
                return is_report_safe(new_head, tail, sign)
            else:
                return False


with open('2024/day2/day2_input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        parts = [int(x) for x in parts]

        head = parts.pop(0)
        tail = parts
        sign = None

        if is_report_safe(head, tail, sign):
            safe += 1

    file.close()

print(safe)
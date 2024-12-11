# day 9
def solve(decrease):
    list = []
    free = []
    file_id = 0
    answer = []
    pos = 0
    for i, c in enumerate(text):
        if i % 2 == 0:
            if decrease:
                list.append((pos, int(c), file_id))
            for i in range(int(c)):
                answer.append(file_id)
                if not decrease:
                    list.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            free.append((pos, int(c)))
            for i in range(int(c)):
                answer.append(None)
                pos += 1

    for (pos, sz, file_id) in reversed(list):
        for space_i, (space_pos, space_sz) in enumerate(free):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert answer[pos + i] == file_id, f'{answer[pos + i]=}'
                    answer[pos + i] = None
                    answer[space_pos + i] = file_id
                free[space_i] = (space_pos + sz, space_sz - sz)
                break

    ans = 0
    for i, c in enumerate(answer):
        if c is not None:
            ans += i * c
    return ans

text = open('inputs/day9_input.txt').read().strip()

count = solve(False)
count2 = solve(True)
print(count)
print(count2)
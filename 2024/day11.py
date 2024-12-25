# day 11
def solve(x, t):
    if (x,t) in dict:
        return dict[(x,t)]

    if t==0:
        ret = 1

    elif x==0:
        ret = solve(1, t-1)

    elif len(str(x))%2==0:
        dstr = str(x)
        left = dstr[:len(dstr)//2]
        right = dstr[len(dstr)//2:]
        left, right = (int(left), int(right))
        ret = solve(left, t-1) + solve(right, t-1)

    else:
        ret = solve(x*2024, t-1)

    dict[(x,t)] = ret
    return ret


def solve_all(t):
    return sum(solve(x, t) for x in text)


count = 0
count2 = 0
text = open('inputs/day11_input.txt').read().strip()
text = [int(x) for x in text.split()]

dict = {}

print(solve_all(25))
print(solve_all(75))
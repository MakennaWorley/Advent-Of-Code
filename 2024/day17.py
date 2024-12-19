# day 17
import re

def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]


def getCombo(x, A=None, B=None, C=None):
    if x in [0, 1, 2, 3]:
        return x
    if x == 4:
        return A if A is not None else -1
    if x == 5:
        return B if B is not None else -1
    if x == 6:
        return C if C is not None else -1
    return -1


def run(Ast, part2):
    A = Ast
    B = 0
    C = 0
    ip = 0
    out = []

    while True:
        if ip >= len(program):
            return out
        cmd = program[ip]
        op = program[ip + 1]
        combo = getCombo(op, A, B, C)

        if cmd == 0:
            A = A // 2 ** combo
            ip += 2

        elif cmd == 1:
            B = B ^ op
            ip += 2

        elif cmd == 2:
            B = combo % 8
            ip += 2

        elif cmd == 3:
            if A != 0:
                ip = op

            else:
                ip += 2

        elif cmd == 4:
            B = B ^ C
            ip += 2

        elif cmd == 5:
            out.append(int(combo % 8))
            ip += 2

        elif cmd == 6:
            B = A // 2 ** combo
            ip += 2

        elif cmd == 7:
            C = A // 2 ** combo
            ip += 2


def find_lowest_A(program):
    Ast = 1
    while True:
        A = Ast * 8
        out = run(A, True)
        if out == program:
            return Ast
        Ast += 1


ans = 0
D = open('inputs/day17_input.txt').read().strip()

regs, program = D.split('\n\n')
A,B,C = ints(regs)
program = program.split(':')[1].strip().split(',')
program = [int(x) for x in program]

part1 = run(A, False)
print(','.join([str(x) for x in part1]))

print(find_lowest_A(program))
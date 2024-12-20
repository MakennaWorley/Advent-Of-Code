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


def run(Ast):
    A = Ast
    B = 0
    C = 0
    ip = 0
    out = []

    while True:
        if ip < 0 or ip >= len(program):
            break
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:
            A = A // (2 ** getCombo(operand, A, B, C))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = getCombo(operand, A, B, C) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand - 2
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            out.append(getCombo(operand, A, B, C) % 8)
        elif opcode == 6:
            B = A // (2 ** getCombo(operand, A, B, C))
        elif opcode == 7:
            C = A // (2 ** getCombo(operand, A, B, C))

        ip += 2

    return out


def find_quine(Ast):
    out = []
    matched = program[-1:]
    Ast = 8 ** 15
    power = 14

    while out != program:
        Ast += 8 ** power
        out = run(Ast)
        if out[-len(matched):] == matched:
            power = max(0, power - 1)
            matched = program[-(len(matched) + 1):]

    return Ast


ans = 0
D = open('inputs/day17_input.txt').read().strip()
matches = [int(x) for x in re.findall(r"\d+", D)]

regs, program = D.split('\n\n')
A,B,C = ints(regs)
program = program.split(':')[1].strip().split(',')
program = [int(x) for x in program]

print(",".join([str(x) for x in run(A)]))

Ast = find_quine(A)
print(Ast)
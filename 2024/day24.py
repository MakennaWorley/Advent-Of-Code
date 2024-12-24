# day 24
import re
from itertools import permutations

def parse_input(inputs):
    initial_values = {}
    gate_instructions = []

    for line in inputs.splitlines():
        if ":" in line:
            wire, value = line.split(": ")
            initial_values[wire] = int(value)

        elif "->" in line:
            gate_instructions.append(line)

    return initial_values, gate_instructions


def evaluate_gate(op, val1, val2):
    if op == "AND":
        return val1 & val2

    elif op == "OR":
        return val1 | val2

    elif op == "XOR":
        return val1 ^ val2


def simulate_circuit(initial_values, gate_instructions):
    wire_values = initial_values.copy()
    unresolved = gate_instructions[:]

    while unresolved:
        next_unresolved = []

        for instruction in unresolved:
            match = re.match(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", instruction)
            if match:
                input1, op, input2, output = match.groups()
                if input1 in wire_values and input2 in wire_values:
                    wire_values[output] = evaluate_gate(op, wire_values[input1], wire_values[input2])

                else:
                    next_unresolved.append(instruction)

        unresolved = next_unresolved

    return wire_values


def compute_decimal_from_z(wire_values):
    z_wires = {k: v for k, v in wire_values.items() if k.startswith("z")}
    sorted_z_bits = [z_wires[f"z{str(i).zfill(2)}"] for i in range(len(z_wires))]
    binary_string = "".join(map(str, sorted_z_bits[::-1]))

    return int(binary_string, 2)


text = open('inputs/day24_input.txt').read().strip()

initial_values, gate_instructions = parse_input(text)
wire_values = simulate_circuit(initial_values, gate_instructions)
count = compute_decimal_from_z(wire_values)

print(count)
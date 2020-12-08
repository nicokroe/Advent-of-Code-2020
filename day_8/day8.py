from pathlib import Path
from time import sleep

class Interpreter():
    def __init__(self, instructions: list[tuple[str, int]], index_to_change: int = None):
        self.instructions = instructions
        self.acc = 0
        self.ip = 0
        self.seen = set()
        if index_to_change is not None:
            instruction, value = self.instructions[index_to_change]
            if instruction == "jmp":
                self.instructions[index_to_change] = ("nop", 0)
            else:
                self.instructions[index_to_change] = ("jmp", value)

    def run(self):
        while self.ip not in self.seen and self.ip < len(instructions):
            instruction, value = self.instructions[self.ip]
            if instruction == "nop":
                self.seen.add(self.ip)
                self.ip += 1
            elif instruction == "acc":
                self.seen.add(self.ip)
                self.acc += value
                self.ip += 1
            elif instruction == "jmp":
                self.seen.add(self.ip)
                self.ip += value
        if self.ip >= len(self.instructions):
            return self.acc, self.ip
        else:
            return self.acc, -1

def find_potentials(instructions: list[tuple[str, int]]) -> set[int]:
    potentials = set()
    for index, instruction in enumerate(instructions):
        if instruction[0] == "jmp" or instruction[0] == "nop":
            potentials.add(index)
    return potentials

def get_input() -> list[tuple[str, int]]:
    input_path = Path(__file__).parent / "input.txt"
    instructions = []
    for line in input_path.open().readlines():
        instruction, value = line.split()
        instructions.append((instruction, int(value)))
    return instructions

instructions = get_input()

# Part 1
interpreter = Interpreter(instructions)
print(f"Part 1: {interpreter.run()[0]}")

# Part 2
potentials = find_potentials(instructions)

for potential in potentials:
    interpreter = Interpreter(instructions.copy(), potential)
    acc, exitcode = interpreter.run()
    if exitcode == len(instructions):
        print(f"Part 2: {acc} Changed instruction at line: {exitcode}")
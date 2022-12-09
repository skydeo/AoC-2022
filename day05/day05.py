import timeit
import os
from collections import deque
from dataclasses import dataclass


@dataclass
class Instruction:
    num: int
    start: int
    end: int


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("day05/05.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()

# print(test_input)


def split_instructions(puzzle_input: list[str]) -> tuple[list[str], list[str]]:
    sep = 0
    for num, line in enumerate(puzzle_input):
        if not line:
            sep = num
            break

    layout = puzzle_input[:sep]
    instructions = puzzle_input[sep + 1 :]

    return (layout, instructions)


def process_instructions(instructions: list[str]) -> list[Instruction]:
    ins = []
    for instruction in instructions:
        _, num, _, start, _, end = instruction.split()
        ins.append(Instruction(num=int(num), start=int(start) - 1, end=int(end) - 1))

    return ins


def layout_to_stacks(layout: list[str]) -> list[deque]:
    num_of_stacks = max(map(int, layout[-1].split()))
    stacks = [deque() for _ in range(num_of_stacks)]
    for row in layout[:-1][::-1]:
        for stack_num, crate_pos in enumerate(range(1, len(row), 4)):
            crate_id = row[crate_pos]
            if crate_id != " ":
                stacks[stack_num].append(crate_id)

    return stacks


def apply_instruction(instruction: Instruction, stacks: list[deque]) -> list[deque]:
    for _ in range(instruction.num):
        crate_id = stacks[instruction.start].pop()
        end_stack = stacks[instruction.end]
        # print(f"Moving {crate_id} from {instruction.start} to {instruction.end}")
        end_stack.append(crate_id)

    return stacks


def find_top_crates(stacks: list[deque]) -> str:
    top_crates = ""
    for stack in stacks:
        top_crates += stack.pop()

    return top_crates


layout, instructions = split_instructions(puzzle_input)
instructions = process_instructions(instructions)
stacks = layout_to_stacks(layout)
for instruction in instructions:
    stacks = apply_instruction(instruction, stacks)
top_crates = find_top_crates(stacks)

print(f"Part 1: {top_crates}")


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

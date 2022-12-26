import timeit
import os
from dataclasses import dataclass


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


@dataclass
class Motion:
    direction: str
    steps: int
    direction_coords: tuple

    direction_translation: dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    direction_coords = direction_translation[direction]


start_time = timeit.default_timer()

with open("day09/09.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitline()

print(test_input)


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

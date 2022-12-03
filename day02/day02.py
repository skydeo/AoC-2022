import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("02.txt", "r+") as f:
    rounds = [tuple(i.split()) for i in f.read().splitlines()]


def calculate_points(elf_choice: str, my_choice: str) -> int:
    choice_points = {"X": 1, "Y": 2, "Z": 3}
    win_points = {
        "X": {"A": 3, "B": 0, "C": 6},
        "Y": {"A": 6, "B": 3, "C": 0},
        "Z": {"A": 0, "B": 6, "C": 3},
    }

    choice_value = choice_points.get(my_choice)
    win_value = win_points.get(my_choice).get(elf_choice)

    return choice_value + win_value


# test_input = [("A", "Y"), ("B", "X"), ("C", "Z")]
# for t in test_input:
#     print(calculate_points(*t))

part_one = sum([calculate_points(*round) for round in rounds])
print(f"Part 1: {part_one}")


def backcalculate_points(elf_choice: str, round_status: str) -> int:
    # x: lose, y: draw, z:win
    choice_points = {"A": 1, "B": 2, "C": 3}
    win_points = {"X": 0, "Y": 3, "Z": 6}
    choice_lookup = {
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
        "Z": {"A": "B", "B": "C", "C": "A"},
    }

    my_choice = choice_lookup.get(round_status).get(elf_choice)
    choice_value = choice_points.get(my_choice)
    win_value = win_points.get(round_status)

    return choice_value + win_value


# test_input = [("A", "Y"), ("B", "X"), ("C", "Z")]
# for t in test_input:
#     print(backcalculate_points(*t))

part_two = sum([backcalculate_points(*round) for round in rounds])
print(f"Part 1: {part_two}")


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

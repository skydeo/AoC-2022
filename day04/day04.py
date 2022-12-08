import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("04.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

data = [t.split(",") for t in puzzle_input]


def check_for_overlap(elf_a: str, elf_b: str) -> bool:
    elf_a_start, elf_a_end = map(int, elf_a.split("-"))
    elf_b_start, elf_b_end = map(int, elf_b.split("-"))

    elf_a_range = set(range(elf_a_start, elf_a_end + 1))
    elf_b_range = set(range(elf_b_start, elf_b_end + 1))

    if all(a in elf_b_range for a in elf_a_range) or all(
        b in elf_a_range for b in elf_b_range
    ):
        return True


overlaps = 0
for elf_a, elf_b in data:
    if check_for_overlap(elf_a, elf_b):
        overlaps += 1

print(f"Part 1: {overlaps} ranges overlap")


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

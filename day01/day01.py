import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("01.txt", "r+") as f:
    puzzle_input = [i for i in f.read().split("\n\n")]

elf_cals = []

for elf in puzzle_input:
    t = [int(cal) for cal in elf.split()]
    elf_cals.append(t)

cal_list = list(map(sum, elf_cals))
max_cals = max(cal_list)

print(f"Part 1: Maximum calories: {max_cals}")
answer_to_clipboard(max_cals)


top_three_sum = sum(sorted(cal_list)[-3:])
print(f"Part 2: Top three elves total calories: {top_three_sum}")
answer_to_clipboard(top_three_sum)


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

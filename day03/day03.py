import os
import string
import timeit


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("03.txt", "r+") as f:
    rucksacks = [i for i in f.read().splitlines()]

test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

alpha = string.ascii_lowercase + string.ascii_uppercase


def find_common_item(rucksack: str) -> str:
    half = int(len(rucksack) / 2)

    compartment_1 = set(rucksack[:half])
    compartment_2 = set(rucksack[half:])

    return compartment_1.intersection(compartment_2).pop()


def lookup_priority(item: str) -> int:
    return alpha.index(item) + 1


priority_sum = sum(
    [lookup_priority(find_common_item(rucksack)) for rucksack in rucksacks]
)

print(f"Part 1: {priority_sum}")


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

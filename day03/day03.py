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


def partition_rucksacks(rucksacks: list) -> list:
    partitioned_rucksacks = []
    for n in range(0, len(rucksacks), 3):
        partitioned_rucksacks.append(rucksacks[n : n + 3])

    return partitioned_rucksacks


def find_badge(rucksack_1: list, rucksack_2: list, rucksack_3: list) -> str:
    r1 = set(rucksack_1)
    r2 = set(rucksack_2)
    r3 = set(rucksack_3)

    return r1.intersection(r2).intersection(r3).pop()


partitioned_rucksacks = partition_rucksacks(rucksacks)
priority_sum = sum(
    [lookup_priority(find_badge(*group)) for group in partitioned_rucksacks]
)

print(f"Part 2: {priority_sum}")

end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

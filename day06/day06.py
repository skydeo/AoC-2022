import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("day06/06.txt", "r+") as f:
    puzzle_input = [i for i in f.read()]

test_input = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

test_input_answers = [7, 5, 6, 10, 11]


def check_tests(test_input, test_input_answers) -> str:
    results = [find_sop_marker_idx(test) for test in test_input]
    for a, b in zip(results, test_input_answers):
        if a != b:
            return f"Test failed. {a} != {b}."
    return "All tests passed."


def find_sop_marker_idx(datastream: str, packet_size: int = 4) -> int:
    for idx, _ in enumerate(datastream[: -(packet_size - 1)]):
        packet = datastream[idx : idx + packet_size]
        if len(set(packet)) == packet_size:
            return idx + packet_size
    return -1


# print(check_tests(test_input, test_input_answers))
sop_marker_idx = find_sop_marker_idx(puzzle_input)

print(f"Part 1: {sop_marker_idx}")


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

import timeit
import os
import io
from dataclasses import dataclass


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("day07/07.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@dataclass
class Directory:
    name: str
    subdirectories: list
    files: list


@dataclass
class Subdirectory(Directory):
    parent_directory: Directory
    subdirectories: Subdirectory


@dataclass
class File:
    name: str
    size: int


def split_blocks(output: str) -> list[str]:
    output: str = io.StringIO(output)
    num_chars: int = output.seek(0, os.SEEK_END)
    output.seek(0, os.SEEK_SET)
    pos: int = output.tell()

    blocks: list = []
    buffer: list = []
    while pos < num_chars:
        line = output.readline().replace("\n", "")
        # print(type(line), line)
        if line[0] == "$":
            if buffer:
                blocks.append(buffer)
            buffer = []
            buffer.append(line)
        else:
            buffer.append(line)

        pos = output.tell()
        # print(pos, num_chars)
    else:
        blocks.append(buffer)

    return blocks


file_tree: dict = {}

output_blocks = split_blocks(test_input)
print(output_blocks)

end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

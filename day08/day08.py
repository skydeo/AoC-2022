import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("day08/08.txt", "r+") as f:
    puzzle_input = [list(i) for i in f.read().splitlines()]

test_input = """30373
25512
65332
33549
35390"""

test_input = [list(line) for line in test_input.splitlines()]
# print(test_input)


def count_visible_trees(tree_grid: list[list[str]]) -> int:
    tree_count = 0
    tree_column_grid = list(map(list, zip(*tree_grid)))
    grid_size = len(tree_grid)
    for row_num, row_data in enumerate(tree_grid):
        for column_num, column in enumerate(row_data):
            if (row_num not in (0, grid_size - 1)) and (
                column_num not in (0, grid_size - 1)
            ):
                tree_height = tree_grid[row_num][column_num]
                # print(f"({column_num}, {row_num}):\t{tree_grid[row_num][column_num]}")
                left = row_data[:column_num]
                right = row_data[column_num + 1 :]
                top = tree_column_grid[column_num][:row_num]
                bottom = tree_column_grid[column_num][row_num + 1 :]

                visible_left = all([tree_height > tree for tree in left])
                visible_right = all([tree_height > tree for tree in right])
                visible_top = all([tree_height > tree for tree in top])
                visible_bottom = all([tree_height > tree for tree in bottom])

                if any([visible_left, visible_right, visible_top, visible_bottom]):
                    tree_count += 1

    tree_count += (grid_size - 1) * 4

    return tree_count


tree_count = count_visible_trees(puzzle_input)
print(f"Part 1: {tree_count}")
# 11041 too high

end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")

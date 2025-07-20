
from typing import List


def maximumGrayness(grid : List[str]) -> int:
    len_y = len(grid)
    len_x = len(grid[0])

    black_rows = [0]*len_y
    black_columns = [0]*len_x

    for y in range(len_y):
        for x in range(len_x):
            if (grid[y][x] == '1'):
                black_rows[y] += 1
                black_columns[x] += 1

    best_grayness = -1
    for y in range(len_y):
        for x in range(len_x):
            blacks = black_rows[y] + black_columns[x]
            whites = len_x + len_y - blacks

            difference = blacks - whites
            best_grayness = max(best_grayness, difference)
            print(blacks, whites, difference, y,x)

    return best_grayness

print(maximumGrayness(["1010","0101","1010"]))

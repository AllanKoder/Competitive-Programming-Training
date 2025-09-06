from collections import defaultdict, deque

n, m, k = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input())


def get_neighbours(y: int, x: int, height: int, width: int) -> list[(int,int)]:
    output = []
    if y >= 1:
        output.append((y-1, x))
    if y < height-1:
        output.append((y+1, x))
    if x >= 1:
        output.append((y, x-1))
    if x < width-1:
        output.append((y, x+1))
    return output

def solve(matrix, k):
    height = len(matrix)
    width = len(matrix[0])

    count_of_periods = 0 
    starter = None
    for y in range(height):
        for x in range(width):
            c = matrix[y][x]
            if c == '.':
                count_of_periods += 1
                starter = (y,x)
    keep_amount = count_of_periods - k 

    stack = [starter]

    kept = 0
    visited = set()
    while kept < keep_amount:
        item = stack.pop()
        y = item[0]
        x = item[1]
        if (item in visited or matrix[y][x] != '.'): continue

        visited.add((item))
        kept += 1
        for n_y, n_x in get_neighbours(y, x, height, width):
            stack.append((n_y, n_x))


    for y in range(height):
        for x in range(width):
            if (matrix[y][x] == '.' and (y,x) not in visited):
                print('X', end='')
                continue
            print(matrix[y][x], end='')
        print()

solve(matrix, k)
    
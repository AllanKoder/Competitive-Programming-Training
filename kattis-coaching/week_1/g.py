x, y = map(int, input().split())

matrix = []
for _ in range(y):
    arr = list(map(int,input().split()))
    matrix.append(arr)

# Invalidate all numbers which are in a group
invalidated = set()
from collections import deque
directions = [[0,1], [0,-1], [1,0], [-1,0]]
def flood_fill(start_y, start_x):
    queue = deque([(start_x, start_y)])
    val = matrix[start_y][start_x]

    while queue:
        current_x, current_y = queue.popleft()
        if (current_x,current_y) in invalidated:
            continue
        if matrix[current_y][current_x] != val:
            continue

        invalidated.add((current_x, current_y))

        for dy, dx in directions:
            new_x = dx + current_x
            new_y = dy + current_y
            if new_x < 0 or new_y < 0 or new_x >= x or new_y >= y:
                continue
            queue.append((new_x, new_y))

def is_riceable(current_y,current_x):
    for dy, dx in directions:
        new_x = dx + current_x
        new_y = dy + current_y
        if new_x < 0 or new_y < 0 or new_x >= x or new_y >= y:
            continue

        if matrix[current_y][current_x] > matrix[new_y][new_x]:
            return False

    return True


for i in range(y):
    for j in range(x):
        if not is_riceable(i,j):
            flood_fill(i,j)

print(x*y - len(invalidated))
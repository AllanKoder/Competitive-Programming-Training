import heapq
R,C,N = map(int, input().split())

pri_queue = []
for i in range(1, N+1):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    pri_queue.append((0, i, (y,x)))

def neighbours(y,x):
    output = []
    if y > 0:
        output.append((y-1,x))
    if x > 0:
        output.append((y,x-1))
    if y < R-1:
        output.append((y+1,x))
    if x < C-1:
        output.append((y,x+1))
    return output

heapq.heapify(pri_queue)
first_matrix = [[(float('inf'), None)]*C for _ in range(R)]
second_matrix = [[(float('inf'), None)]*C for _ in range(R)]
count = [[0]*C for _ in range(R)]
visited = set()
while pri_queue:
    dist, label, cord = heapq.heappop(pri_queue)
    y = cord[0]
    x = cord[1]

    if count[y][x] >= 2:
        continue
    if (label, cord) in visited:
        continue
    visited.add((label, cord))
    count[y][x] += 1
    # Save to matrix
    if first_matrix[y][x][1] is None:
        first_matrix[y][x] = (dist, label)
    elif first_matrix[y][x][1] != label:
        if second_matrix[y][x][1] is None:
            second_matrix[y][x] = (dist, label)
    else:
        continue

    for neighbour in neighbours(y, x):
        heapq.heappush(pri_queue, (dist+1, label, neighbour))

def matrix_print(matrix):
    def fun(s):
        return (str(s[1]))
    for row in matrix:
        print(" ".join(map(fun, row)))

matrix_print(first_matrix)
matrix_print(second_matrix)


    

    
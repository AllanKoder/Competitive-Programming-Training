from collections import deque
import bisect

n,m = map(int, input().split())

divisibles = []
q = m
was_odd = 0
distance = 0
while q > 0:
    new_num = q + was_odd
    divisibles.append((new_num, distance))
    was_odd = 1 if new_num % 2 == 1 else 0
    distance += 1 if new_num % 2 == 0 else 2
    q = new_num // 2

divisibles.reverse()
def bfs(n,m):
    answer = float('inf')
    queue = deque([(n, 0)])

    while queue:
        item = queue.popleft()

        # Consider moving back to a divisible item if possible
        fst, _ = zip(*divisibles)
        position = bisect.bisect_right(fst, item[0])
        if position > 0:
            actual_index = position-1
            new_position_from_sub = divisibles[actual_index][0]
            diff = item[0] - new_position_from_sub
            total_moves = diff + item[1] + divisibles[actual_index][1]

            answer = min(answer, total_moves)

        # Consider multiplying
        if (item[0] < m):
            queue.append((item[0]*2, item[1] + 1))



    return answer

print(bfs(n,m))


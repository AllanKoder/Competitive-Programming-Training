from collections import defaultdict, deque

v, e = map(int, input().split())
path = input()

adj = defaultdict(list)
in_degrees = defaultdict(int)

for _ in range(e):
    from_i, to_i = map(int, input().split())
    adj[from_i].append(to_i)
    in_degrees[to_i] += 1

zeroes = deque([])
for k in adj:
    if in_degrees[k] == 0:
        zeroes.append(k)

best = [-float('inf')]*v
best[0] = 0

while zeroes:
    current = zeroes.popleft()

    for neighbor in adj[current]:
        addition = 1 if path[neighbor] == 'X' else -1
        if neighbor == v-1:
            addition = 0

        best[neighbor] = max(best[neighbor], addition + best[current])

        in_degrees[neighbor] -= 1
        if in_degrees[neighbor] == 0:
            zeroes.append(neighbor)

print(best[v-1])
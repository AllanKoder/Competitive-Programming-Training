v,e = map(int, input().split())
trail = input()
paths = []

for _ in range(e):
    from_pos, to_pos = map(int, input().split())
    paths.append((from_pos, to_pos))

paths.sort()

max_happiness = [-1]*v
max_happiness[0] = 0

for from_pos, to_pos in paths:
    if max_happiness[from_pos] == -1:
        continue
    
    addition = 0
    if to_pos < v-1:
        addition = 1 if trail[to_pos] == 'X' else -1

    new_happiness = addition + max_happiness[from_pos]
    if max_happiness[to_pos] == -1:
        max_happiness[to_pos] = new_happiness 
    else:
        max_happiness[to_pos] = max(max_happiness[to_pos], new_happiness)

print(max_happiness[v-1])
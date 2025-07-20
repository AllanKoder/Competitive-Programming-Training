import functools

n = int(input())
arr = list(map(int, input().split()))

@functools.lru_cache(None)
def solve(i, chosen_activity):
    if i >= len(arr):
        return 0

    vacation = arr[i]
    spots = set()
    if vacation == 1:
        spots.add(1)
    if vacation == 2:
        spots.add(2)
    if vacation == 3:
        spots.add(1)
        spots.add(2)

    best_choice = -1
    for options in range(1, 3):
        bonus = 1 if chosen_activity in spots else 0
        for next_activity in range(1,3):
            if next_activity == chosen_activity and bonus == 1: continue
            best_choice = max(bonus + solve(i+1, next_activity), best_choice)

    return best_choice

best = max([solve(0, 1), solve(0, 2)])
print(n - best)

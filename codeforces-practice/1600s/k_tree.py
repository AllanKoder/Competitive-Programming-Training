import functools

target, k, d_min = map(int, input().split())

@functools.lru_cache(None)
def solve(current_sum, used):
    if current_sum == target and used:
        return 1
    if current_sum >= target:
        return 0
    
    count = 0
    for i in range(1, k+1):
        count += solve(current_sum+i, used if used else i >= d_min)
    
    return count % (10**9 + 7 )

print(solve(0, False))


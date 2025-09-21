from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)

n = int(input())

nums = list(map(int, input().split()))

@lru_cache(None)
def dp(i, last):
    val = 1

    for j in range(i+1, len(nums)):
        if nums[i] + nums[last] == nums[j]:
            val = max(val, 1 + dp(j, i))
    
    return val


if len(nums) == 1:
    print(1)
else:
    best = 2
    for last in range(n):
        for start in range(last+1, n):
            best = max(best, dp(start, last) + 1)

    print(best)
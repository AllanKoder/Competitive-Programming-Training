from itertools import permutations
from functools import lru_cache
import sys
sys.setrecursionlimit(10**9)

suits = "hdcs"

s = input()

def longest(sequence):
    dp = [[0] * 4 for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(4):
            if i > 0:
                dp[i][j] = dp[i-1][j]

            if s[i] == sequence[j]:
                dp[i][j] = max(dp[i][j], 1 + dp[i-1][j])
            
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])

    return max(dp[-1])

# @lru_cache(None)
# def longest_sub_sequence(i, j, sequence):
#     if j >= len(sequence):
#         return 0
#     if i >= len(s):
#         return 0
    
#     best = longest_sub_sequence(i+1, j, sequence)

#     if s[i] == sequence[j]:
#         best = max(best, 1 + longest_sub_sequence(i+1, j, sequence))

#     best = max(best, longest_sub_sequence(i, j+1, sequence))

#     return best

best = -float('inf')
for p in permutations(suits):
    best = max(best,longest(p))

print(len(s) - best)

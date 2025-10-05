from functools import lru_cache
import sys

sys.setrecursionlimit(10**4)

MOD = 10**9 + 7

def solve(l, r, d, m):
    R = str(r)
    n = len(R)
    L = str(l)
    L = L.zfill(n)

    pow10 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow10[i] = (pow10[i-1] * 10) % m
    @lru_cache(None)
    def dp(i, is_low, is_high, mod) -> int:
        # Num of magic numbers
        if i >= n:
            return 1 if mod == 0 else 0
        
        low_limit = int(L[i]) if is_low else 0
        high_limit = int(R[i]) if is_high else 9

        is_even = (i+1) % 2 == 0
        count = 0
        for j in range(low_limit, high_limit+1):
            if is_even and j != d:
                continue
            if not is_even and j == d:
                continue

            is_next_high = is_high and j == high_limit
            is_next_low = is_low and j == low_limit

            next_mod = (pow10[n - i - 1] * j) % m
            next_mod = (next_mod + mod) % m
            suffix_count = dp(i+1, is_next_low, is_next_high, next_mod)
            count = (count + suffix_count) % MOD

        return count

    return dp(0, True, True, 0)

m,d = map(int, input().split())
l = int(input())
r = int(input())

print(solve(l, r, d, m))


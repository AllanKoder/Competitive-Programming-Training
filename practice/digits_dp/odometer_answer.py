
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)
num = ""


@lru_cache(maxsize=None)
def solve_dp(pos, k, under, started, targ, targ2):
    """
    Recursive digit DP with memoization.
    pos     : index in the number string
    k       : balance counter (shifted by +20 initially)
    under   : already below upper bound (bool)
    started : whether number has started (bool)
    targ    : target digit
    targ2   : second target digit or -1
    """
    if pos == len(num):
        if not started:
            return 0
        if targ2 != -1:
            return 1 if k == 20 else 0
        return 1 if k >= 20 else 0

    ans = 0
    limit = int(num[pos])
    for i in range(10):
        if not under and i > limit:
            break

        is_under = under or (i < limit)
        is_started = started or (i != 0)

        if is_started and targ2 != -1 and i != targ and i != targ2:
            continue

        new_k = k
        if is_started:
            if i == targ:
                new_k = k + 1
            else:
                new_k = k - 1

        ans += solve_dp(pos + 1, new_k, is_under, is_started, targ, targ2)

    return ans


def count_interesting_to(ubound):
    """Count interesting numbers up to ubound inclusive."""
    global num
    num = str(ubound)

    ans = 0
    for i in range(10):
        solve_dp.cache_clear()
        ans += solve_dp(0, 20, False, False, i, -1)

    duplicates = 0
    for i in range(10):
        for j in range(10):
            solve_dp.cache_clear()
            duplicates += solve_dp(0, 20, False, False, i, j)

    return ans - (duplicates // 2)


def main():
    
    X, Y = map(int, input().split())
    result = count_interesting_to(Y) - count_interesting_to(X - 1)
    print(result)

if __name__ == "__main__":
    main()

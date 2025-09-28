from functools import lru_cache

t = int(input())

def solve(x):
    if x <= 0:
        return (1, 0)

    stringed = str(x)
    length = len(stringed)

    @lru_cache(None)
    def dp(n,c):
        # returns (count, sum)
        if n >= length:
            return (1, 0)
        sum_output = 0

        limit = int(stringed[n]) if c else 9
        total_count = 0
        for i in range(limit+1):
            next_is_constrained = True if (c and i == limit) else False
            new_count, new_sum = dp(n+1, next_is_constrained)
            sum_output += (i * new_count) + new_sum
            total_count += new_count
        return (total_count, sum_output)
    return dp(0, True)

while t > 0:
    l, r = map(int, input().split())
    _, s_r = solve(r)
    _, s_l = solve(l-1)
    print(s_r - s_l)

    t -= 1
from functools import lru_cache

def solve(l, r):
    R = str(r)
    n = len(R)
    L = str(l)
    L = L.zfill(n)

    @lru_cache(None)
    def dp(i, is_started, is_low, is_high):
        # Num of possibilities, num of zeroes
        if i >= n:
            if is_started == False:
                # All zeroes
                return 1, 1
            else:
                # No zeroes
                return 1, 0
        
        low_limit = int(L[i]) if is_low else 0
        high_limit = int(R[i]) if is_high else 9

        num_count = 0
        zeroes_count = 0
        for j in range(low_limit, high_limit+1):
            is_next_high = is_high and j == high_limit
            is_next_low = is_low and j == low_limit
            is_started = is_started or j > 0

            
            suffix_nums, suffix_zeroes = dp(i+1, is_started, is_next_low, is_next_high)

            num_count += suffix_nums
            zeroes_count += suffix_zeroes
            if is_started and j == 0:
                zeroes_count += suffix_nums
        
        return num_count, zeroes_count

    return dp(0, False, True, True)[1]

while True:
    l, r = map(int, input().split())
    if l == -1 or r == -1:
        break
    print(solve(l, r))


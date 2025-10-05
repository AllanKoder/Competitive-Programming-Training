
def solve(r):
    R = str(r)
    n = len(R)
    if r < 0: 
        return 0
    
    # States = i, tight, leading
    # Returns: nums, and zeroes
    dp = [[[(0,0)]*2 for _ in range(2)] for _ in range(n+1)]
    for is_tight in range(2):
        for is_leading in range(2):
            if is_leading:
                dp[n][is_tight][is_leading] = (1, 1)
            else:
                # Is an "empty num"
                dp[n][is_tight][is_leading] = (1, 0)

    for is_tight in range(2):
        for is_leading in range(2):
            for i in range(n-1, -1, -1):
                count_zeroes = 0
                count_nums = 0
                high_limit = 9 if not is_tight else int(R[i])
                for j in range(high_limit+1):
                    is_next_leading = is_leading and j == 0
                    is_next_tight = is_tight and j == high_limit

                    suffix_nums, suffix_zeros = dp[i+1][is_next_tight][is_next_leading]

                    count_nums += suffix_nums
                    count_zeroes += suffix_zeros

                    if j == 0 and not is_leading:
                        count_zeroes += suffix_nums

                dp[i][is_tight][is_leading] = (count_nums, count_zeroes)

    result = dp[0][1][1][1]
    return result
while True:
    l, r = map(int, input().split())
    if l == -1 or r == -1:
        break
    print(solve(r) - solve(l-1))


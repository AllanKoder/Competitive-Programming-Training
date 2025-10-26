

n = int(input())

def min_push_pop(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # length 1 substrings
    for i in range(n):
        dp[i][i] = 2  # push + pop for one char

    # fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Option 1: handle s[i] separately
            best = 2 + dp[i + 1][j]

            # Option 2: reuse s[i] with a matching s[k]
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    best = min(best, dp[i + 1][k - 1] + dp[k][j])

            dp[i][j] = best

    return dp[0][n - 1]


for _ in range(n):
    s = input()
    print(len(s) + min_push_pop(s))
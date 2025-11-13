def mult(t1, mul):
    return [t1[i] * mul for i in range(3)]

r, s, p = map(int, input().split())

# dp[r][s][p] = [prob_R, prob_S, prob_P]
dp = [[[ [0.0, 0.0, 0.0] for _ in range(p+1)] for _ in range(s+1)] for _ in range(r+1)]

# Base cases
for i in range(1, r+1):
    dp[i][0][0] = [1.0, 0.0, 0.0]
for j in range(1, s+1):
    dp[0][j][0] = [0.0, 1.0, 0.0]
for k in range(1, p+1):
    dp[0][0][k] = [0.0, 0.0, 1.0]

# Fill DP table
for i in range(r+1):
    for j in range(s+1):
        for k in range(p+1):
            # Skip base cases
            if (i == 0 and j == 0) or (j == 0 and k == 0) or (i == 0 and k == 0):
                continue

            total = i*j + j*k + k*i
            if total == 0:
                continue

            # Combine from previous states
            if i > 0 and j > 0:
                for t in range(3):
                    dp[i][j][k][t] += dp[i][j-1][k][t] * (i*j) / total
            if j > 0 and k > 0:
                for t in range(3):
                    dp[i][j][k][t] += dp[i][j][k-1][t] * (j*k) / total
            if k > 0 and i > 0:
                for t in range(3):
                    dp[i][j][k][t] += dp[i-1][j][k][t] * (k*i) / total

print(*dp[r][s][p])

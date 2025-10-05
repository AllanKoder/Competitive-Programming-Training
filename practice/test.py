n = int(input())

dp = [0]*(n+1)
dp[0] = 1
# dp[i] = dp[i-1] + dp[i-2]
# dp[i+2] = dp[i+1] + dp[i]

for i in range(n+1):
    for j in range(1,3):
        if i+j > n:
            break
        dp[i+j] += dp[i]

print(dp)
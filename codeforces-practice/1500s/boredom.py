from collections import defaultdict

t = int(input())

arr = list(map(int, input().split()))
n = max(arr)

# Preprocessing
scores = defaultdict(int)

for a in arr:
    # Turn to 0 indexed
    scores[a-1] += a

dp = defaultdict(int)
for i in range(n+1):
    dp[i] = max(dp[i-1], scores[i] + dp[i-2])

print(dp[n])
import sys
sys.setrecursionlimit(10**9)

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


dp = [[0]*2 for _ in range(n+1)] 
for i in range(n-1, -1, -1):
    best_nothing_choice = max(dp[i+1][0], dp[i+1][1])
    
    dp[i][1] = max(best_nothing_choice, arr2[i] + dp[i+1][0])
    dp[i][0] = max(best_nothing_choice, arr1[i] + dp[i+1][1])

print(max(dp[0][0], dp[0][1]))
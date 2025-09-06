n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def cost(target_medium, arr):
    total_cost = 0
    medium = len(arr)//2
    for i in range(medium, len(arr)):
        total_cost += max(0, target_medium - arr[i])
    return total_cost

def solve():
    l, r = 0, 10**9 + k
    while l <= r:
        target_m = (l+r)//2
        if cost(target_m, arr) <= k:
            l = target_m + 1
        else:
            r = target_m - 1
    
    return max(0, l-1)

print(solve())
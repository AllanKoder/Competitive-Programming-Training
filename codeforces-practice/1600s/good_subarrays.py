from collections import defaultdict

t = int(input())

def solve(arr):
    n = len(arr)

    counter = defaultdict(int)

    total = 0
    summing = 0
    for i in range(0,n+1):
        if i > 0:
            summing += arr[i-1]
        total += counter[summing - i]
        counter[summing - i] += 1
    return total

for _ in range(t):
    input()
    arr = list(map(int,input()))
    print(solve(arr))

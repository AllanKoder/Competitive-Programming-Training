t = int(input())

def solve(arr):
    n = len(arr)
    diff = [0]*n

    sum1 = 0
    sum2 = 0

    visited = set()
    for i in range(n):
        if i % 2 == 0:
            sum1 += arr[i]
        else:
            sum2 += arr[i]

        diff = sum1-sum2
        if diff == 0 or diff in visited:
            return True
        visited.add(diff)

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if solve(a) else "NO")


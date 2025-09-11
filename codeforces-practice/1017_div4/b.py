
t = int(input())

def solve(m,l,r):
    leftmost = min(0,l)
    rightmost = max(0,r)


    left = 0
    right = 0
    total = 0

    while left > leftmost and total < m:
        left -= 1
        total += 1
    while right < rightmost and total < m:
        right += 1
        total += 1

    return [left, right]

for _ in range(t):
    n, m, l, r = map(int, input().split())

    ans = solve(m,l,r)
    print(ans[0], ans[1])
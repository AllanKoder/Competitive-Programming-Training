n = int(input())

for _ in range(n):
    p, r, f = map(float, input().split())
    p = int(p)
    f = int(f)
    years = 0

    while p <= f:
        p = int(p * r)
        years += 1

    print(years)
n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

last_day = 0
for a, b in arr:
    if b >= last_day:
        last_day = b
    else:
        last_day = a

print(last_day)

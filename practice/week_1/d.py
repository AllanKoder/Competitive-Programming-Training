t = int(input())
starts, ends = [], []

for _ in range(t):
    s, e = map(int, input().split())
    starts.append(s)
    ends.append(e)

L = max(starts)
R = min(ends)

if L > R:
    print("bad news")
else:
    print(R - L + 1, L)

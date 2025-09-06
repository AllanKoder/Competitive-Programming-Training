count = int(input())
for _ in range(count):
    i = int(input())
    v = 360/(180 -i)
    if (int(v) == v):
        print("YES")
    else:
        print("NO")

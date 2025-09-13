t = int(input())


for _ in range(t):
    n, v = map(int, input().split())

    octal = 0
    try:
        octal = int(str(v), 8)
    except:
        pass
    decim = v
    hex = 0
    try:
        hex = int(str(v), 16)
    except:
        pass

    print(n, octal, decim, hex)
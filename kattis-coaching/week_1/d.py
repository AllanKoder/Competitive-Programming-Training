uapc = "UAPC"
current = set(uapc)
s = input()

for c in s:
    current.remove(c)

for c in uapc:
    if c in current:
        print(c,end="")

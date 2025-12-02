a = input()

def zFunction(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            k = i - l

            # Case 2: reuse the previously computed value
            z[i] = min(r - i + 1, z[k])

        # Try to extend the Z-box beyond r
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update the [l, r] window if extended
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z
print(zFunction("baaaabaaaa"))


def is_repeated(num: int):
    stringed = str(num)
    n = len(stringed)
    z = zFunction(stringed)

    for p in range(1, n):
        if n % p == 0 and z[p] == n - p:
            return True

    return False


total = 0
ids = a.split(",")
for id in ids:
    first,last = id.split("-")
    first = int(first)
    last = int(last)

    for i in range(first, last+1):
        if is_repeated(i):
            total += i

print(total)

def count_zeroes_upto(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1      # "0" itself has exactly one '0' digit

    res = 0
    pos = 1
    while pos <= n:
        high = n // (pos * 10)
        curr = (n // pos) % 10
        low = n % pos

        if curr == 0:
            res += (high - 1) * pos + (low + 1)
        else:
            res += high * pos

        pos *= 10

    return res + 1     # add the zero from the number 0 itself


# main loop (same as yours)
import sys
for line in sys.stdin:
    l, r = map(int, line.split())
    if l == -1 and r == -1:
        break
    print(count_zeroes_upto(r) - count_zeroes_upto(l - 1))

MOD = 998244353
N = 100005

# Precompute powers of 2 modulo MOD
s = [1] * N
for i in range(1, N):
    s[i] = s[i - 1] * 2 % MOD

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    res = []
    i = j = 0  # Indices of max in p and q so far
    for k in range(n):
        if p[k] > p[i]:
            i = k
        if q[k] > q[j]:
            j = k
        if p[i] != q[j]:
            if p[i] > q[j]:
                val = (s[p[i]] + s[q[k - i]]) % MOD
            else:
                val = (s[q[j]] + s[p[k - j]]) % MOD
        else:
            val = (s[p[i]] + s[max(q[k - i], p[k - j])]) % MOD
        res.append(val)

    print(*res)

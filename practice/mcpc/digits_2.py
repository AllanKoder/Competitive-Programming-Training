MOD = 10**9 + 7

def count_supersets(a, m):
    bits_m = m.bit_length()
    dp = {True: 1, False: 0}
    for i in reversed(range(bits_m)):
        bit_m = (m >> i) & 1
        bit_a = (a >> i) & 1
        newdp = {True: 0, False: 0}
        for tight, ways in dp.items():
            if bit_a == 1:
                if bit_m == 0 and tight:
                    continue
                new_tight = tight and (bit_m == 1)
                newdp[new_tight] = (newdp[new_tight] + ways) % MOD
            else:
                limit = bit_m if tight else 1
                for b in range(limit+1):
                    new_tight = tight and (b == bit_m)
                    newdp[new_tight] = (newdp[new_tight] + ways) % MOD
        dp = newdp
    return (dp[True] + dp[False]) % MOD


n, k, m = map(int, input().split())

print(count_supersets(n,k,m))
MOD = 10**9 + 7

def solve(r, l, d, m):
    R = str(r)
    n = len(R)
    L = str(l)

    # States = i, tight_high, tight_low, mod
    dp = [[[[0]*m for _ in range(2)] for _ in range(2)] for _ in range(n+1)]

    pow10s = [1]*n
    current_pow = 1
    for i in range( n):
        pow10s[i] = current_pow
        current_pow = (current_pow * 10) % m

    dp[0][1][1][0] = 1

    for i in range(0, n):
        for i_mod in range(m):
            for is_tight_h in range(2):
                for is_tight_l in range(2):
                    
                    is_even = (i+1)%2==0

                    current_count = dp[i][is_tight_l][is_tight_h][i_mod]
                    if not current_count: continue

                    high_limit = int(R[i]) if is_tight_h else 9 
                    low_limit = int(L[i]) if is_tight_l else 0
                    for j in range(low_limit, high_limit+1):
                        if is_even and j != d:
                            continue
                        if not is_even and j == d:
                            continue

                        next_tight_h = is_tight_h and j == int(R[i])
                        next_tight_l = is_tight_l and j == int(L[i])

                        next_mod = (j * pow10s[n-i-1] + i_mod) % m
                        dp[i+1][next_tight_l][next_tight_h][next_mod] = (current_count + 
                                                                         dp[i+1][next_tight_l][next_tight_h][next_mod]) % MOD
    
    ans = 0
     
    for is_tight_h in range(2):
        for is_tight_l in range(2):
            ans = (ans + dp[n][is_tight_l][is_tight_h][0])%MOD

    return ans

m,d = map(int,input().split())
l = int(input())
r = int(input())

print(solve(r,l,d,m))
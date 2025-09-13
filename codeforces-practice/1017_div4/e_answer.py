from collections import defaultdict
t = int(input())


def summing(ones_d, n, num):
    total = 0
    for i in range(0, 31):
        ones = ones_d[i]
        zeroes = n - ones

        base = 2**i

        # It is containing a 0 bit on the spot
        if (num & (2**i)) == 0:
            total += ones * base 
        else:
            total += zeroes * base
    return total

def solve(arr, n):
    ones_d = defaultdict(int)
    for v in arr:
        for i in range(0, 31):
            if (v & (2**i)) != 0:
                ones_d[i] += 1
        
    return max(summing(ones_d, n, a) for a in arr) 

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))
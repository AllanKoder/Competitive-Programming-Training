import math

def solve(n, k, m):
    N = n # students
    K = k # min 1-bits

    max_string = bin(m)[2:]
    length = len(max_string)
    def search(i, tight, ones, placeable_zeroes, debug_string):
        if i == length:
            if ones < K:
                return 0

            return math.perm(placeable_zeroes, N)

        limit = 1 if not tight else int(max_string[i])
        ways = 0
        for j in range(limit+1):
            next_tight = tight and str(j) == max_string[i]
            
            add_zeroes = 0
            if not tight or (tight and int(max_string[i]) == 1 and j == 0):
                add_zeroes = int(j == 0)

            ways += search(i+1, next_tight, ones + int(j == 1), add_zeroes + placeable_zeroes, debug_string + str(j))
        
        return ways
    return search(0, True, 0, 0, "")
            

n, k, m = map(int, input().split())

print(solve(n,k,m))
import math

def solve(n, k, m):
    N = n # students
    K = k # min 1-bits

    max_string = bin(m)[2:]
    length = len(max_string)
    print(max_string, "MAX_STRING")
    def search(i, tight, ones_tight, ones, placeable_zeroes, debug_string):
        if i == length:
            if ones < K:
                return 0
            if placeable_zeroes < N:
                return 0

            output = math.perm(2**placeable_zeroes, N)
            print(debug_string, placeable_zeroes, output)
            return output

        limit = 1 if not tight else int(max_string[i])
        ways = 0
        for j in range(limit+1):
            next_tight = tight and str(j) == max_string[i]

            if j == 0 and (not tight or j < int(max_string[i])):
                add_zeroes = 1
            else:
                add_zeroes = 0

            next_ones_tight = ones_tight and add_zeroes == 1
            ways += search(i+1, next_tight, next_ones_tight, ones + int(j == 1), add_zeroes + placeable_zeroes, debug_string + str(j))
        
        return ways
    return search(0, True, True, 0, 0, "")
            

n, k, m = map(int, input().split())

print(solve(n,k,m))
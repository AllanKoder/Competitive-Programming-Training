n,m = map(int, input().split())

def pairs(x):
    return (x * (x-1))//2

def max_friends(n,m):
    max_for_one = n - m + 1
    return pairs(max_for_one)

def min_friends(n,m):
    min_divided = n // m
    leftover = n % m

    return pairs(min_divided)*(m-leftover) + pairs(min_divided+1)*leftover

print(min_friends(n,m), max_friends(n,m))


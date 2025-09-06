n,m = map(int, input().split())

def min_operations(n, m):
    count = 0
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        count += 1
    return count + (n - m)

print(min_operations(n,m))

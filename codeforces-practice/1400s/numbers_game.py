from functools import lru_cache

t = int(input())

def odd_divisors(n):
    i = 3
    while i < n:
        if n % i == 0:
            yield i
        i += 2

@lru_cache(None)
def ash(i):
    if i == 1: return False
    if i == 2: return True
    if i % 2 == 1:
        return True
    for d in odd_divisors(i):
        # if any of the choices makes fast lose, then choose that choice
        if fast(int(i/d)) == False:
            return True
            
    
    return False

@lru_cache(None)
def fast(i):
    if i == 1: return False
    if i == 2: return True
    if i % 2 == 1:
        return True
    for d in odd_divisors(i):
        # if any of the choices makes ash lose, then choose that choice
        if ash(int(i/d)) == False:
            return True

    return False


for _ in range(t):
    n = int(input())
    print("Ashishgup" if ash(n) else "FastestFinger")
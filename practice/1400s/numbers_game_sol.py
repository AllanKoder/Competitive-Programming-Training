import math

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def winner(n):
    if n == 1:
        return "FastestFinger"
    if n == 2:
        return "Ashishgup"
    if n % 2 == 1:
        return "Ashishgup"
    if (n & (n - 1)) == 0:  # power of 2
        return "FastestFinger"
    if n % 4 != 0 and is_prime(n // 2):
        return "FastestFinger"
    return "Ashishgup"

t = int(input())
for _ in range(t):
    n = int(input())
    print(winner(n))

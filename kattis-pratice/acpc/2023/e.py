import math

def raster_square_area(W, H):
    # sum_{i=1}^H floor(i*W/H)
    S = (W-1)*(H-1)//2 + math.gcd(W, H) - 1 + W//H * H
    return 4 * S

print(raster_square_area(12, 4))

def floor_sum(n: int, m: int, a: int, b: int) -> int:
    """
        Compute sum_{i=0}^{n-1} floor((a*i + b) / m).
        n: The number of terms to sum over (i = 0 to n-1).
        m: The divisor in the floor division. Must be positive.
        a: The coefficient multiplying i in the numerator.
        b: The constant term added in the numerator.
    """
    ans = 0
    while True:
        if a >= m:
            q = a // m
            ans += (n - 1) * n * q // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            break
        # reduce parameters (Euclidean-style)
        n, m, a, b = y_max // m, a, m, y_max % m
    return ans


# Example:
W = 12
K = 5
print(floor_sum(W + 1, K, 2, 0))

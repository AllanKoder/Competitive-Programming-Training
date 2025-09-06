import functools

n = int(input())

@functools.lru_cache(None)
def is_divisible_1s(n, i):
    if n % 11 == 0:
        return True
    if n < 11:
        return False
    if i <= 2:
        return False
    longest_ones = int('1' * i) 

    is_valid = False
    for j in range(0, 11):
        minus = longest_ones * j
        if minus > n: break
        new_number = n - minus
        is_valid = is_valid or is_divisible_1s(new_number, i-1)
    
    return is_valid

for i in range(n):
    number = int(input())
    length = len(str(number))
    is_divisible = is_divisible_1s(number, length)
    print("YES" if is_divisible else "NO")

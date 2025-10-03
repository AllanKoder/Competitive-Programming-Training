def divisors(n):
    i = 1
    output = []
    while i * i <= n:
        if n % i == 0:
            output.append(i)
            if i != n // i:
                output.append(n // i)
        i += 1
    output.remove(n)
    return output

while True:
    try:
        n = int(input())
        ds = divisors(n)
        s = sum(ds)

        if s == n:
            print(n, "perfect")
        elif abs(s - n) <= 2:
            print(n, "almost perfect")
        else:
            print(n, "not perfect")

    except EOFError:
        break

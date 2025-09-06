import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []

    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        total = n * m
        grid = [[0] * m for _ in range(n)]

        # Case 1: m is composite (or even)
        if not is_prime(m):
            # simple row-by-row
            for i in range(n):
                base = i * m
                for j in range(m):
                    grid[i][j] = base + j + 1

        # Case 2: m is prime but n is composite
        elif not is_prime(n):
            # column-by-column
            for j in range(m):
                base = j * n
                for i in range(n):
                    grid[i][j] = base + i + 1

        # Case 3: both m and n are prime
        else:
            step = 2 * m
            for i in range(n):
                offset = (i * step) % total
                for j in range(m):
                    grid[i][j] = (offset + j) % total + 1

        # collect output
        for row in grid:
            out.append(" ".join(map(str, row)))

    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    threading.Thread(target=main).start()

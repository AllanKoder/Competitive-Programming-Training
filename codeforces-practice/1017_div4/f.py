t = int(input())


def solve(n,m,k):
    start = 0
    counter = start
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = counter + 1

            counter += 1
            counter = counter % k

            if counter == start:
                start += 1
                counter = start

    return (matrix)

for _ in range(t):
    n,m,k = map(int, input().split())

    ans = solve(n,m,k)

    for row in ans:
        print(" ".join(str(a) for a in row))
t = int(input())

def solve(n, matrix):
    result = []
    N = 2*n
    d = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            index = (i + j)
            if index not in d:
                d[index] = int(matrix[i-1][j-1])
    
    output = []
    not_in = set(range(1, N+1))
    for i in range(2, N+1):
        output.append(int(d[i]))
        not_in.remove(int(d[i]))
    output.insert(0, list(not_in)[0])

    return " ".join(str(a) for a in output)
for _ in range(t):
    n = int(input())

    matrix = []
    for _ in range(n):
        line = input()
        matrix.append(list(map(int, line.split())))

    print(solve(n, matrix))
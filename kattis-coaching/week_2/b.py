n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))


output = []
for from_j in range(n):
    for to_i in range(n):
        if matrix[from_j][to_i] >= 0:
            output.append((from_j+1, to_i+1, matrix[from_j][to_i]))

output.sort()
print(len(output))
for a,b,c in output:
    print(a,b,c)
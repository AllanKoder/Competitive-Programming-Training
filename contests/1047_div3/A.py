t = int(input())

for _ in range(t):
    k, x = map(int, input().split())
    
    multiplied = 2**k * x
    print(multiplied)

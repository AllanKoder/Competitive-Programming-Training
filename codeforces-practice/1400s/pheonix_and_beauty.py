t = int(input())

def solve(arr, k):
    uniques = set(arr)
    if len(uniques) > k:
        print("-1")
        return
    
    run = sorted(list(uniques))
    while len(run) < k:
        run.append(1)
    
    answer = run*len(arr)

    print(len(answer))
    print(" ".join(map(str,answer)))
    

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(arr, k)
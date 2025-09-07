t = int(input())

def solve(arr):
    answer = []
    highest = max(arr)
    

    for i in range(len(arr)):
        element = arr[i]
        answer.append(highest - element + 1)
    
    return (str(a) for a in answer) 

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(" ".join(solve(arr)))

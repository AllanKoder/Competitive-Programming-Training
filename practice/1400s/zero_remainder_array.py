from collections import Counter
t = int(input())

def solve(arr, k):
    new_arr = [x % k for x in arr]
    new_arr = list(filter(lambda x : x % k != 0, new_arr))
    if len(new_arr) == 0:
        return 0
    
    c = Counter(new_arr)
    key, loops = max(c.items(), key=lambda x: (x[1], -x[0]))
    moves_needed = (loops-1)*k + (k-key)
    return moves_needed + 1 

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int,input().split()))
    print(solve(arr, k))
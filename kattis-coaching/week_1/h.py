import sys
sys.setrecursionlimit(10**9)
import bisect
n, k = map(int, input().split())
arr = list(map(int,input().split()))

def jumps(i, jump_size):
    if i >= len(arr)-1:
        return 0

    current_num = arr[i]
    next_jump = bisect.bisect_right(arr, current_num+jump_size)-1
    if next_jump > i:
        how_many = jumps(next_jump, jump_size)
        if how_many >= 0:
            return 1 + how_many

    return -1


l,r = 1, 10**6
answer = -1
while l <= r:
    jump_power = (l+r)//2
    how_many_jumps = jumps(0, jump_power)
    if how_many_jumps == -1:
        l = jump_power+1
    elif how_many_jumps == k:
        answer = max(answer, jump_power)
        l = jump_power+1
    elif how_many_jumps < k:
        r = jump_power-1
    elif how_many_jumps > k:
        l = jump_power+1

print(answer)
        

import bisect

n = int(input())
nums = list(map(int, input().split()))
nums.sort()


def range_sum(l,r):
    i_l = bisect.bisect_left(nums, l)
    i_r = bisect.bisect_right(nums, r)

    return i_r - i_l

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(range_sum(l,r))
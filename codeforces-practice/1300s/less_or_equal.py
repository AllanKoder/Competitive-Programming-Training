input()
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))

res = []

def bisect_right(nums, x):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r)//2
        if (nums[m] > x):
            r = m
        else:
            l = m + 1
    return l

for i in b:
    res.append(str(bisect_right(a, i)))

print(" ".join(res))

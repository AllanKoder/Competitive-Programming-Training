import bisect

n = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

arr = [a_arr[i] - b_arr[i] for i in range(n)]
arr.sort()


total = 0
for i in range(n-1):
    if arr[i] >= 1:
        total += n - i - 1
        continue

    ideal_add = -arr[i] + 1

    location = bisect.bisect_left(arr, ideal_add)
    total += n - location

print(total)



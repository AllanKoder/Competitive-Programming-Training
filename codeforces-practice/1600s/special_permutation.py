import bisect

t = int(input())


def construct_perm(n, start):
    if n < 4: return []

    arr = list(range(1, n+1))
    current_num = start - 3
    output = []
    while len(arr) > 0:
        while len(arr) > 0 and arr[-1] - current_num > 2 and current_num + 3 in arr:
            current_num += 3
            arr.remove(current_num)
            output.append(current_num)

        # Next num to the left min
        if len(arr) > 0:
            left_thing = bisect.bisect_right(arr, current_num - 2) - 1
            if (left_thing < len(arr)):
                current_num = arr[left_thing]
                arr.remove(current_num)
                output.append(current_num)

    return output

def is_diff_two(arr):
    for i in range(len(arr)-1):
        if not (2 <= abs(arr[i] - arr[i+1]) <= 4):
            return False
    return True

for _ in range(t):
    n = int(input())
    if n < 4:
        print(-1)
        continue
    for start in range(1,5):
        a = construct_perm(n, start)
        if is_diff_two(a):
            print(" ".join(str(b) for b in a))
            break


"""
Mistakes:
- I realized we can do jump from evens increasing, then odds decreasing. But, after 
realizing that there is a jump of 1, I gave up.
- I started trying more complex ideas
- I didn't test with the easy automated testing method 

Takeaways:
- On blockages, don't discard the whole idea, figure out what insights are worth keeping,
and know where I went wrong
- When something is too complex, step back
- Always test if you are not sure.

"""
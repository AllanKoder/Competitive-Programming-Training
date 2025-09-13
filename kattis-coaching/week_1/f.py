t = int(input())

arr = []
for _ in range(t):
    x = int(input())
    arr.append(x)
arr.sort()

best = 0
for i in range(len(arr)):
    potential_h = arr[i]
    # Is a valid H since the rest is greater than potential H
    rest_length = len(arr) - i
    if rest_length >= potential_h:
        best = max(best, potential_h)
    
    if potential_h > rest_length:
        best= max(best, rest_length)
print(best)
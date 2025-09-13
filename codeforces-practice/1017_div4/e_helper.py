arr = list(map(int, input().split()))

def summing(arr,selected):
    total = 0
    for a in arr:
        total += a^selected
    return total

for a in arr:
    print(summing(arr, a))


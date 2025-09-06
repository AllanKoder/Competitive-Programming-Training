n, k = map(int, input().split())

a = list(map(int,input().split()))

def solve(arr):
    arr.sort()
    middle = len(arr)//2

    adds_left = k
    current_number = arr[middle]
    for index in range(middle, len(arr)-1):
        if adds_left == 0: break

        numbers_to_add = index - middle + 1
        purchase = arr[index+1] - current_number

        amount_to_increase = 0
        if purchase * numbers_to_add > adds_left:
            amount_to_increase = adds_left // numbers_to_add
            adds_left = 0 
        else:
            amount_to_increase = purchase
            adds_left -= numbers_to_add * purchase
        current_number += amount_to_increase

    
    return current_number + (adds_left // (len(arr) - middle))

print(solve(a))
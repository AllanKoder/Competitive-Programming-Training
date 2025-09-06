
def get_best_even_sum(array):
    array.sort(reverse=True)
    smallest_odd = float('inf')
    best = 0

    # If it is a positive small odd, sub it
    # If it is a negative small odd, sub the abs of it 
    for n in array:
        if n > 0:
            best += n
            if n % 2 != 0:
                smallest_odd = min(smallest_odd, n)
        if n % 2 != 0:
            if abs(n) < smallest_odd:
                smallest_odd = abs(n)
                break

    if best % 2 == 0:
        return best
    else:
        return best - smallest_odd

print(get_best_even_sum([-1,-2,-3,8,7]))
print(get_best_even_sum([6,3,4,-1,9,17]))
print(get_best_even_sum([2,3,6,10,1]))
print(get_best_even_sum([-1,-2,-2,-4,-5,19]))

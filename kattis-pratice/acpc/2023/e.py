import math

# area formula
k, w = map(int, input().split())
rise = math.floor(w*2/k)
length = rise + w


def triangle_area(w, k, rise):
    remainder = w % k
    smaller_rise = rise-1

    odds_sum = 0
    evens_sum = 0

    if rise > 1:
        odds = smaller_rise-1 if (smaller_rise-1)%2 == 1 else smaller_rise
        evens = smaller_rise-1 if (smaller_rise-1)%2 == 0 else smaller_rise

        odds_sum = ((odds+1)*(odds//2 + 1))//2 * math.floor(k/2)
        evens_sum = ((evens)*(evens//2 + 1))//2 * math.ceil(k/2)
    
    width_of_top = remainder - math.ceil(k/2) if rise % 2 == 1 else remainder
    remainder_sum = rise * width_of_top

    return remainder_sum + odds_sum + evens_sum

t_area = triangle_area(w,k,rise)

area = (length**2 - t_area*4) % (10**9+9)
print(area)

import functools
m,s = map(int, input().split())
# Want to get max number that reaches target_sum

@functools.lru_cache(None)
def dp(digits, target_sum):
    if digits == 1 and target_sum < 10 and target_sum > 0:
        return target_sum
    if digits == 1 and target_sum == 0:
        return 0
    if digits == 0:
        return None

    best_number = -1
    for i in range(9, -1, -1):
        potential_best = dp(digits - 1, target_sum - i)
        if potential_best:
            new_number = int(str(potential_best) + str(i))
            best_number = max(best_number, new_number)

    return best_number if best_number > 0 else None

max_ans = dp(m, s)
if max_ans == None:
    print(-1, -1)
else:
    list_min_ans = list(str(max_ans)[::-1])
    i = 0
    while list_min_ans[0] == '0' and i < len(list_min_ans):
        list_min_ans[i], list_min_ans[0] = list_min_ans[0], list_min_ans[i]
        i += 1

    min_ans = "".join(list_min_ans)
    print(str(min_ans), max_ans)



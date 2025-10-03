import functools

def best_in_range(l: int, r: int):
    L, R = str(l), str(r)
    n = len(R)
    L = L.zfill(n)  # pad l with zeros to align with r

    @functools.lru_cache(None)
    def dp(pos, tight_low, tight_high, leading):
        if pos == n:
            return (0, "") if leading else (1, "")

        lo = int(L[pos]) if tight_low else 0
        hi = int(R[pos]) if tight_high else 9

        best = (0, "")
        for d in range(lo, hi+1):
            new_low = tight_low and d == lo
            new_high = tight_high and d == hi
            new_leading = leading and d == 0

            sub_prod, sub_num = dp(pos+1, new_low, new_high, new_leading)

            if new_leading:
                cand_prod = sub_prod
                cand_num = sub_num
            else:
                cand_prod = (d if sub_prod > 0 else d) * sub_prod if sub_prod else d
                cand_num = str(d) + sub_num

            if cand_prod > best[0] or (cand_prod == best[0] and cand_num > best[1]):
                best = (cand_prod, cand_num)

        return best

    return dp(0, True, True, True)[1]


l, r = map(int, input().split())
print(best_in_range(l, r))

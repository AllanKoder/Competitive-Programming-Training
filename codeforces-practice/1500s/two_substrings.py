
# s = input()
# n = len(s)
# @lru_cache(None)
# def solve(i:int, found_ab:bool = False, found_ba:bool = False) -> bool:
#     if found_ab and found_ba:
#         return True

#     if i >= n:
#         return False
    
#     has_strings = False
#     if s[i:i+2] == "AB" and not found_ab:
#         has_strings = has_strings or solve(i+2, True, found_ba)
#     if s[i:i+2] == "BA" and not found_ba:
#         has_strings = has_strings or solve(i+2, found_ab, True)

#     has_strings = has_strings or solve(i+1, found_ab, found_ba)

#     return has_strings


# def solve_iterative(s: str) -> bool:
#     n = len(s)
#     stack = [(0, False, False)]   # (i, found_ab, found_ba)
#     visited = set()

#     while stack:
#         i, found_ab, found_ba = stack.pop()

#         # If we've already visited this state, skip it
#         if (i, found_ab, found_ba) in visited:
#             continue
#         visited.add((i, found_ab, found_ba))

#         # If we already found both substrings → success
#         if found_ab and found_ba:
#             return True

#         # If we are past the end -> no success from this path
#         if i >= n:
#             continue

#         # Try a jump of +2 if we match "AB"
#         if s[i:i+2] == "AB" and not found_ab:
#             stack.append((i+2, True, found_ba))

#         # Try a jump of +2 if we match "BA"
#         if s[i:i+2] == "BA" and not found_ba:
#             stack.append((i+2, found_ab, True))

#         # Try moving just +1 without marking anything
#         stack.append((i+1, found_ab, found_ba))

#     return False


def solve_bottom_up(s:str) -> bool:
    n = len(s)
    dp = [[[False]*(2) for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        for a in range(2):
            for b in range(2):
                if not dp[i][a][b]:
                    continue
                    
                if a and b:
                    return True
                
                if i >= n:
                    continue

                dp[i+1][a][b] = True

                if i < n-1 and s[i:i+2] == "AB":
                    dp[i+2][1][b] = True

                if i < n-1 and s[i:i+2] == "BA":
                    dp[i+2][a][1] = True
                
    for i in range(n + 1):
        if dp[i][1][1]:
            return True

print("YES" if solve_bottom_up(s) else "NO")


    
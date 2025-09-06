from collections import Counter

def cost(burgers: int, burger_recipe: Counter, n: list[int], p: list[int]):
    return max(0, burgers*burger_recipe[0] - n[0]) * p[0] + \
        max(0, burgers*burger_recipe[1] - n[1]) * p[1] +  \
        max(0, burgers*burger_recipe[2] - n[2]) * p[2]

def solve(burger_recipe: Counter, n: list[int], p: list[int], total_budget: int) -> int:    
    # binary search to find max number of burgers while cost < total_budget
    l,r = 0, 10**13
    answer = 0 
    while l <= r:
        burgers = (l + r) // 2
        if cost(burgers, burger_recipe, n, p) <= total_budget:
            l = burgers + 1
            answer = burgers
        else:
            r = burgers - 1
    return answer

    
raw_burger = input()
raw_burger = raw_burger.replace("B", "0")
raw_burger = raw_burger.replace("S", "1")
raw_burger = raw_burger.replace("C", "2")
burger_recipe = Counter(map(int, raw_burger))
n = list(map(int, input().split()))
p = list(map(int, input().split()))
r = int(input())

print(solve(burger_recipe, n, p, r))
from collections import Counter

def determine_remaining_buy(money: int, burger: Counter, p: list[int]) -> int:
    cost_of_burger = 0
    for k, count in burger.items():
        cost_of_burger += count * p[k]

    if cost_of_burger == 0:
        return 0
    return money // cost_of_burger

def solve(burger: Counter, n: list[int], p: list[int], r: int) -> int:
    total_money = r
    burger_count = 0

    while not all([n[x] == 0 for x in range(len(n)) if burger[x] > 0]):
        for i in range(len(n)):
            if burger[i] == 0: continue

            if n[i] < burger[i]:
                diff = burger[i] - n[i]
                needed_money = diff * p[i] 
                if needed_money > total_money:
                    return burger_count
                total_money -= needed_money
                n[i] = 0
            else:
                n[i] -= burger[i]
        burger_count += 1
    

    remaining_buy = determine_remaining_buy(total_money, burger, p)

    return burger_count + remaining_buy

raw_burger = input()
raw_burger = raw_burger.replace("B", "0")
raw_burger = raw_burger.replace("S", "1")
raw_burger = raw_burger.replace("C", "2")
burger = Counter(map(int, raw_burger))
n = list(map(int, input().split()))
p = list(map(int, input().split()))
r = int(input())

print(solve(burger, n, p, r))

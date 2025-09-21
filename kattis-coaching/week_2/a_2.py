k,r = map(int, input().split())
ingredients = list(map(int, input().split()))

recipes = []
for _ in range(r):
    recipes.append(list(map(int, input().split())))

best_profit = 0

for r in recipes:
    max_smoothies = float('inf')
    for i in range(k):
        if r[i] == 0:
            continue
        max_smoothies = min(max_smoothies, ingredients[i]//r[i])
    best_profit = max(best_profit, max_smoothies * r[-1])

print(best_profit)

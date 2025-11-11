import sys
import functools
sys.setrecursionlimit(10**9)

INF = 10**18

def main():
    input = sys.stdin.readline

    N, M, B = map(int, input().split())
    prices = []
    needs = []
    solars = []

    for _ in range(N):
        p, r, g = map(int, input().split())
        prices.append(p)
        needs.append(r)
        solars.append(g)

    sell_prices = [list(map(int, input().split())) for _ in range(N)]
    sell_amounts = [list(map(int, input().split())) for _ in range(N)]


    @functools.lru_cache(None)
    def dp(i, b):
        if i >= N:
            return 0
        plans = [(0,0)] + list(zip(sell_amounts[i], sell_prices[i]))
        smallest = float('inf')
        for next_b in range(0, B+1):
            for sell_amount, sell_price in plans:
                amount_energy = b + solars[i]
                energy_needed = sell_amount + needs[i] + next_b
                to_buy = max(energy_needed-amount_energy, 0)
                cost = dp(i+1, next_b) + to_buy *prices[i] - sell_price
                smallest = min(smallest, cost)
        return smallest

    print(dp(0, 0))


main()
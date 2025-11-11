import sys

INF = 10**18

def main():
    input = sys.stdin.readline

    N, M, C = map(int, input().split())
    prices = []
    needs = []
    solars = []

    for _ in range(N):
        p, r, g = map(int, input().split())
        prices.append(p)
        needs.append(r)
        solars.append(g)

    # Next N lines: M integers = sell prices (revenue)
    sell_prices = [list(map(int, input().split())) for _ in range(N)]
    # Next N lines: M integers = sell amounts
    sell_amounts = [list(map(int, input().split())) for _ in range(N)]

    # DP initialization
    dp = [[INF] * (C + 1) for _ in range(N + 1)]
    dp[0][0] = 0  # battery starts empty, no cost yet

    for i in range(1, N + 1):
        price = prices[i - 1]
        need = needs[i - 1]
        solar = solars[i - 1]

        # include "no plan" option
        plans = [(0, 0)] + list(zip(sell_amounts[i - 1], sell_prices[i - 1]))

        for b_prev in range(C + 1):
            if dp[i - 1][b_prev] == INF:
                continue

            for sell_amt, sell_price in plans:
                for b_next in range(C + 1):
                    total_required = need + sell_amt + b_next
                    available = b_prev + solar
                    to_buy = max(0, total_required - available)
                    cost = dp[i - 1][b_prev] + price * to_buy - sell_price
                    dp[i][b_next] = min(dp[i][b_next], cost)

    print(min(dp[N]))


if __name__ == "__main__":
    main()

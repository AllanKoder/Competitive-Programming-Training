import copy
a, b, c = map(int, input().split())

def solve():
    global a,b,c
    l = [b,c]
    results = [a]
    for i in range(2):
        next_results = []
        for value in list(results):
            for c in ["-", "+", "/", "*"]:
                if c == "-":
                    output = value - l[i]
                    next_results.append(output)

                if c == "+":
                    output = value + l[i]
                    next_results.append(output)

                if c == "/" and l[i] != 0 and value % l[i] == 0:
                    output = value // l[i]
                    next_results.append(output)

                if c == "*":
                    output = value * l[i]
                    next_results.append(output)
        results = copy.copy(next_results)
        next_results = []

    return results

ans = solve()

smallest = float('inf')
for r in ans:
    if r >= 0:
        smallest = min(smallest, r)

print(smallest)
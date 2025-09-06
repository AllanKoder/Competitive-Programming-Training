m, s = map(int, input().split())

# Edge case: s == 0
if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
    exit()

# Check if it's even possible to form such a number
if s > 9 * m:
    print("-1 -1")
    exit()

# --- Construct smallest number ---
sum_left = s
smallest = ""
for i in range(m):
    for d in range(0 if i != 0 else 1, 10):
        if sum_left - d <= 9 * (m - i - 1):
            smallest += str(d)
            sum_left -= d
            break

# --- Construct largest number ---
sum_left = s
largest = ""
for i in range(m):
    for d in range(9, -1, -1):
        if sum_left - d >= 0 and sum_left - d <= 9 * (m - i - 1):
            largest += str(d)
            sum_left -= d
            break

print(f"{smallest} {largest}")

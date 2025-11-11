from collections import Counter

n = int(input())
s = input()

all = (set(s))

l = 0
r = 0
current = Counter()

def contains(current):
    for k in all:
        if k not in current or current[k] <= 0:
            return False
        
    return True

smallest = float('inf')
while r < len(s):
    current[s[r]] += 1
    while contains(current):
        smallest = min(smallest, r-l+1)
        current[s[l]] -= 1
        l += 1
    r += 1

print(smallest)
from collections import Counter
t = int(input())

def solve(arr):
    c = Counter(arr)
    for k, v in c.items():
        if v % k != 0:
            print(-1)
            return
    number_id = 0

    m = {}
    m_usage = {}
    result = []

    for c in arr:
        if m.get(c) == None:
            number_id += 1
            m[c] = number_id

        id = m[c]
        m_usage[id] = m_usage.get(id, 0) + 1
        if m_usage[id] == c:
            m[c] = None
            m_usage[id] = 0

        result.append(id)
    print(" ".join(list(str(a) for a in result)))

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(arr)
    

    
    
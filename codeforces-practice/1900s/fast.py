import math


n, l, v1, v2, k = map(int, input().split())

def valid(t):
    gap = (l - v1*t)
    bus_duration = gap/(v2-v1) # seconds to reach remaining side (relative)
    if bus_duration <= 0:
        return True

    groups = math.ceil(n / k)
    time_back = gap/(v2+v1)

    total_time = bus_duration * groups + time_back * (groups - 1)

    if total_time <= t:
        return True
    return False

    # Total time is: time there * count, time back * count-1


def search(l, r, c):
    if c >= 100:
        return l
    m = (l+r)/2
    if valid(m):
        return search(l, m, c+1)
    return search(m, r, c+1)


print(search(0, 10e9, 0))
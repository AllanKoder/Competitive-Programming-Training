def biggest_num(n,k):
    if k >= n:
        return 1
    groups = 2
    best_groups = n
    best_value = 1
    while groups*groups <= n:
        if n % groups == 0:
            if n/groups >= best_value and n/groups <= k:
                best_value = n//groups
                best_groups = groups
            if groups >= best_value and groups <= k:
                best_value = groups
                best_groups = n//groups

        groups += 1

    return best_groups

n = int(input())
for _ in range(n):
    n, k = map(int,input().split())
    print(biggest_num(n,k))


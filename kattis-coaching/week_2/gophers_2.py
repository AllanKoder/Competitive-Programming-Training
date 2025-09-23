import math
from collections import defaultdict

try:
    while True:

        # gophers, holes, seconds, velocity
        n,m,s,v = map(int, input().split())

        gophers = []
        for _ in range(n):
            x,y = map(float, input().split())
            gophers.append((x,y))


        holes = []
        for _ in range(m):
            x,y = map(float, input().split())
            holes.append((x,y))

        def can_reach(coord1, coord2):
            possible_dist = s*v
            actual_dist = math.dist(coord1, coord2)
            return possible_dist >= actual_dist

        edges = defaultdict(list)
        for gopher in range(n):
            for hole in range(m):
                if can_reach(gophers[gopher], holes[hole]):
                    edges[gopher].append(hole)


        match = [-1] * m 
        def dfs(u, visited):
            for h in edges[u]:
                if visited[h]:
                    continue
                visited[h] = True
                if match[h] == -1 or dfs(match[h], visited):
                    match[h] = u
                    return True
            return False

        matched = 0
        for g in range(n):
            visited = [False] * m
            if dfs(g, visited):
                matched += 1

        print(n - matched)
except:
    pass
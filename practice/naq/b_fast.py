from collections import deque
import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
towers = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**9

# For each cell: [(dist1, id1), (dist2, id2)]
dist1 = [[INF]*C for _ in range(R)]
id1   = [[-1]*C for _ in range(R)]
dist2 = [[INF]*C for _ in range(R)]
id2   = [[-1]*C for _ in range(R)]

q = deque()
for i, (r, c) in enumerate(towers, start=1):
    r -= 1
    c -= 1
    dist1[r][c] = 0
    id1[r][c] = i
    q.append((r, c, i))

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r, c, tid = q.popleft()
    d = dist1[r][c] if id1[r][c] == tid else dist2[r][c]
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C:
            nd = d + 1

            # Case 1: better than current best
            if nd < dist1[nr][nc] or (nd == dist1[nr][nc] and tid < id1[nr][nc]):
                # push old best down to second-best if it's different
                if id1[nr][nc] != tid:
                    dist2[nr][nc], id2[nr][nc] = dist1[nr][nc], id1[nr][nc]
                dist1[nr][nc], id1[nr][nc] = nd, tid
                q.append((nr, nc, tid))

            # Case 2: better than current second best and not same tower
            elif (tid != id1[nr][nc]) and (
                nd < dist2[nr][nc] or (nd == dist2[nr][nc] and tid < id2[nr][nc])
            ):
                dist2[nr][nc], id2[nr][nc] = nd, tid
                q.append((nr, nc, tid))

# Output results
for r in range(R):
    print(" ".join(map(str, id1[r])))
for r in range(R):
    print(" ".join(map(str, id2[r])))

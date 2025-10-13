from collections import deque
import sys
input = sys.stdin.readline

INF = 10**9

R, C, K = map(int, input().split())
towers = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

best_dist = [[INF]*C for _ in range(R)]
best_id = [[0]*C for _ in range(R)]
second_dist = [[INF]*C for _ in range(R)]
second_id = [[0]*C for _ in range(R)]

# Bucket BFS (distance layers)
q = deque()
for tid, (r, c) in enumerate(towers, start=1):
    best_dist[r][c] = 0
    best_id[r][c] = tid
    q.append((r, c, tid))

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r, c, tid = q.popleft()
    d = best_dist[r][c]

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < R and 0 <= nc < C):
            continue

        nd = d + 1

        # Update first
        if nd < best_dist[nr][nc] or (nd == best_dist[nr][nc] and tid < best_id[nr][nc]):
            # Move previous best to second if needed
            if best_id[nr][nc] != 0:
                sd, sid = best_dist[nr][nc], best_id[nr][nc]
                if sd < second_dist[nr][nc] or (sd == second_dist[nr][nc] and sid < second_id[nr][nc]):
                    second_dist[nr][nc], second_id[nr][nc] = sd, sid

            best_dist[nr][nc], best_id[nr][nc] = nd, tid
            q.append((nr, nc, tid))

        # Update second-best
        elif tid != best_id[nr][nc] and (nd < second_dist[nr][nc] or (nd == second_dist[nr][nc] and tid < second_id[nr][nc])):
            second_dist[nr][nc], second_id[nr][nc] = nd, tid
            q.append((nr, nc, tid))

# Output
out = []
for r in range(R):
    out.append(" ".join(map(str, best_id[r])))
for r in range(R):
    out.append(" ".join(map(str, second_id[r])))

sys.stdout.write("\n".join(out))

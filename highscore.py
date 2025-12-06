import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

INF = 10**30
dist = [-INF] * (n + 1)
dist[1] = 0

for _ in range(n - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] > -INF and dist[u] + w > dist[v]:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        break

good = [False] * (n + 1)
for u, v, w in edges:
    if dist[u] > -INF and dist[u] + w > dist[v]:
        good[v] = True

adj = [[] for _ in range(n + 1)]
for u, v, w in edges:
    adj[u].append(v)

q = deque()
for i in range(1, n + 1):
    if good[i]:
        q.append(i)

vis = [False] * (n + 1)
while q:
    u = q.popleft()
    vis[u] = True
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            q.append(v)

if vis[n]:
    print(-1)
else:
    print(dist[n])

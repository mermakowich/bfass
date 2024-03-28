n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
used = [[False for _ in range(m)] for _ in range(n)]




for i in range(n):
    s = g[i][0]
    for k in s:
        if k == "#":
            bfs(k)

def bfs(x):
    used[x] = True
    q = [x]
    dist[x] = 1
    while len(q)!=0:
        y = q.pop(0)
        for to in g[y]:
            if not used[to]:
                q.append(to)
                dist[to] = dist[y] + 1
                used[to] = True
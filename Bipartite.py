n, m = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
mark = (n+1)*[False]
color = (n+1)*[0]
bipartite = True


def dfs(v, parent):
    mark[v] = True
    if parent == -1:
        color[v] = 1
    else:
        color[v] = 1 - color[parent]
    for u in adj[v]:
        if not mark[u]:
            dfs(u, v)
        elif color[u] == color[v]:
            global bipartite
            bipartite = False


for i in range(1, n+1):
    if mark[i]:
        continue
    dfs(i, -1)

if bipartite:
    print("Graph is Bipartite")
else:
    print("Graph is not Bipartite")

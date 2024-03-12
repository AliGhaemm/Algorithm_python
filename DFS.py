n, m = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
mark = (n+1)*[False]
component = list()
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(v):
    mark[v] = True
    component.append(v)
    for u in adj[v]:
        if not mark[u]:
            dfs(u)


for i in range(1,n+1):
    if mark[i]:
        continue
    component.clear()
    dfs(i)
    print(component)

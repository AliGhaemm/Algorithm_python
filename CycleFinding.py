n, m = map(int, input().split())
adj = list()
for i in range(n+1):
    adj.append(list())
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

cycle_found = False
mark = (n+1)*[False]


def dfs(root, parent):
    mark[root] = True
    for u in adj[root]:
        if not mark[u]:
            dfs(u, root)
        elif u != parent:
            global cycle_found
            cycle_found = True


for i in range(1, n+1):
    if mark[i]:
        continue
    dfs(i, -1)
    if cycle_found:
        print("Graph has cycle")
    else:
        print("Graph doesnt have cycle")

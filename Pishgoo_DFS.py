import sys
sys.setrecursionlimit(10**5 + 100)
n, m = map(int, input().split())
s, t = map(int, input().split())
adj = list()
mark = (n+1)*[False]
for i in range(n+1):
    adj.append(list())
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
isConnected = False


def dfs(v):
    mark[v] = True
    for u in adj[v]:
        if not mark[u]:
            dfs(u)


dfs(s)
if mark[t]:
    print("YES")
else:
    print("NO")

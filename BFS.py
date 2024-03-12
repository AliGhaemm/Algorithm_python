n, m = map(int, input().split())
adj = list()
for i in range(n+10):
    adj.append(list())
distance = (n+10)*[10**9]
queue = list()
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def bfs(root):
    distance[root] = 0
    queue.append(root)
    while queue:
        v = queue.pop()
        for u in adj[v]:
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v]+1
                queue.append(u)


bfs(1)
for i in range(1, n+1):
    print(i, ':', distance[i])

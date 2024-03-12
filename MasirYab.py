n, m = map(int, input().split())
s, t = map(int, input().split())
adj = list()
for i in range(n+10):
    adj.append(list())
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
distance = (n+10)*[10**9]
queue = list()


def bfs(root, destiny):
    distance[root] = 0
    queue.append(root)
    cond = True
    while queue and cond:
        v = queue.pop()
        for u in adj[v]:
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v]+1
                queue.append(u)
            if u == destiny:
                cond = False
                break


bfs(s, t)
if distance[t] == 10**9:
    print(-1)
else:
    print(distance[t])
    queue = [t]
    ans = []
    while queue[0] != s:
        ans.append(queue[0])
        temp = queue.pop()
        for u in adj[temp]:
            if distance[u] < distance[temp]:
                queue.append(u)
    ans.append(s)
    ans.reverse()
    print(*ans)

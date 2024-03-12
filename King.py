from itertools import permutations
import math
n = int(input())
arr = list(map(int, input().split()))
donbale = list(permutations(range(1, n+1)))
edge = list()


def mabna_factorial(lst):
    s = 0
    for i, element in enumerate(lst):
        s += math.factorial(i+1)*element
    return s


for i in donbale:
    edge.append(mabna_factorial(i))
adj = list()
for i in range(len(edge)):
    adj.append(list())


def change(lst, x):
    output = lst[x::-1]
    output += lst[x+1:]
    return output


for i in range(n):
    for j, element in enumerate(donbale):
        if change(donbale[i], j+1) == element:
            adj[i].append(j)
            adj[j].append(i)

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


for i, e in enumerate(donbale):
    if e == arr:
        bfs(edge[i], edge[0])
        break
if distance[0] == 10**9:
    print(-1)
else:
    print(distance)

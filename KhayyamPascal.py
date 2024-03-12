q = int(input())
n = [0]*q
r = [0]*q
for i in range(q):
    n[i], r[i] = list(map(int, input().split()))

c = [[0 for _ in range(2001)] for _ in range(2001)]

for k in range(2001):
    for a in range(k+1):
        if a == 0 or a == k:
            c[k][a] = 1
        else:
            c[k][a] = (c[k-1][a] + c[k-1][a-1]) % (7 + 10**9)

for i in range(q):
    print(c[n[i]][r[i]])

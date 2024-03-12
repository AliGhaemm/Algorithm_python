def process(arr):
    n = len(arr)
    s = 0
    ps = [0 for _ in range(n)]
    for ind in range(n):
        s += arr[ind]
        ps[ind] = s
    return ps


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
L = [None for _ in range(q)]
R = [None for _ in range(q)]
for i in range(q):
    L[i], R[i] = list(map(int, input().split()))
pre_processed = process(a)
for i in range(q):
    print(pre_processed[R[i]] - pre_processed[L[i]] + a[L[i]])

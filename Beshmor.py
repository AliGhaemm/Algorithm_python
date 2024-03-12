T = int(input())
for i in range(T):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ps = [0 for _ in range(n)]
    ps[0] = arr[0]
    for j in range(1, n):
        ps[j] = arr[j] + ps[j-1]

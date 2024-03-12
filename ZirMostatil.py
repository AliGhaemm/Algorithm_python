def sum_range_query(arr, row_num, col_num):
    for i in range(1, row_num):
        for j in range(col_num):
            arr[i][j] += arr[i-1][j]
    return arr


n, m = list(map(int, input().split()))
arr = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr[i][:] = list(map(int, input().split(' ')))
sum_range_query(arr, n, m)
maximum = float('-inf')
for r1 in range(n):
    for r2 in range(r1, n):
        if r1 != 0:
            b = [None for _ in range(m)]
            for i in range(m):
                b[i] = arr[r2][i] - arr[r1-1][i]
        else:
            b = [None for _ in range(m)]
            for i in range(m):
                b[i] = arr[r2][i]
        ans = float('-inf')
        maxsum = [0] * m
        maxsum[0] = b[0]
        for v in range(1, m):
            maxsum[v] = max(maxsum[v - 1] + b[v], b[v])
        for z in range(m):
            ans = max(ans, maxsum[z])
        if ans >= maximum:
            maximum = ans


print(maximum)

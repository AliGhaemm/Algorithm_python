n, m = list(map(int, input().split()))
arr = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr[i][:] = list(map(int, input().split()))
dp = [[None for _ in range(m)] for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + arr[0][i]
dp[1][0] = dp[0][0] + arr[1][0]
for j in range(1, n):
    for i in range(1, m):
        if dp[j][i-1] < dp[j-1][i]:
            dp[j][i] = dp[j][i-1] + arr[j][i]
        else:
            dp[j][i] = dp[j-1][i] + arr[j][i]

print(dp)
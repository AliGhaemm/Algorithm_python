n, m = list(map(int, input().split()))
arr = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr[i][:] = list(map(int, input().split()))

dp = [[None for _ in range(m)] for _ in range(n)]
move = [[None for _ in range(m)] for _ in range(n)]
dp[n-1][0] = arr[n-1][0]
dp[n-1][1] = arr[n-1][0] + arr[n-1][1]
move[n-1][1] = 'R'
dp[n-2][0] = arr[n-1][0] + arr[n-2][0]
move[n-2][0] = 'U'
for i in range(2, m):
    dp[n-1][i] = dp[n-1][i-1] + arr[n-1][i]
    move[n-1][i] = 'R'
for i in range(n-3, -1, -1):
    dp[i][0] = dp[i+1][0] + arr[i][0]
    move[i][0] = 'U'

for i in range(n-2, -1, -1):
    for j in range(1, m):
        if dp[i][j-1] > dp[i+1][j]:
            dp[i][j] = dp[i][j-1] + arr[i][j]
            move[i][j] = 'R'
        else:
            dp[i][j] = dp[i+1][j] + arr[i][j]
            move[i][j] = 'U'

print(dp[0][m-1])
col = m-1
row = 0
steps = ""
while (row, col) != (n-1, 0):
    if move[row][col] == 'R':
        steps += "R"
        col -= 1
    else:
        steps += "U"
        row += 1
print(steps[::-1])

def print_chess(arr):
    for i in range(len(arr)):
        print(arr[i][:])


n, k = list(map(int, input().split()))
chess = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        chess[i][j] = 0


def isTahdid (arr, row, col):
    num = 0
    for i in range(n):
        num += arr[row][i]
        if num > 1: return True
    for i in range(n):
        num += arr[i][col]
        if num > 1: return True
    temp_row = row
    temp_col = col
    while temp_row > 0 and temp_col < n-1:
        num += arr[row-1][col+1]
        temp_row -= 1
        temp_col += 1
        if num > 0: return True
    temp_row = row
    temp_col = col
    while temp_row > 0 and temp_col > 0:
        num += arr[row - 1][col - 1]
        temp_row -= 1
        temp_col -= 1
        if num > 0: return True
    temp_row = row
    temp_col = col
    while temp_row < n-1 and temp_col < n - 1:
        num += arr[row + 1][col + 1]
        temp_row += 1
        temp_col += 1
        if num > 0: return True
    temp_row = row
    temp_col = col
    while temp_row > n-1 and temp_col > 0:
        num += arr[row - 1][col + 1]
        temp_row += 1
        temp_col -= 1
        if num > 0: return True
    return False



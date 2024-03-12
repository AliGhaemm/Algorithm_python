def plot_sudoko(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print()


def is_valid(arr, item, row, col):
    for x in range(9):
        if arr[row][x] == item:
            return False

    for x in range(9):
        if arr[x][col] == item:
            return False
    for i in range(3):
        for j in range(3):
            if arr[i + (row - row % 3)][j + (col - col % 3)] == item:
                return False
    return True


def find_solution(S, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if S[row][col] > 0:
        return find_solution(S, row, col + 1)
    for x in range(1, 10, 1):
        if is_valid(S, x, row, col):
            S[row][col] = x
            if find_solution(S, row, col + 1):
                return True
        S[row][col] = 0
    return False


n = 9
arr = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i][:] = list(map(int, input().split()))
if find_solution(arr, 0, 0):
    plot_sudoko(arr)
else:
    print('this sudoku is not solvable')

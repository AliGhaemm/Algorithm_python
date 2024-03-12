import MergeSort

n, k = list(map(int, input().split()))
arr = [[None for _ in range(n)] for _ in range(k)]
for i in range(k):
    arr[i][:] = list(map(int, input().split()))



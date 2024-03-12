def Jadval(arr, n, k):
    if k == 1:
        return [['.']]




n, k = list(map(int, input().split()))
arr = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i][:] = [*input()]

length = n**k
# final_arr = [[None for _ in range(length)] for _ in range(length)]

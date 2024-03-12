n = int(input())
arr = [None for _ in range(n)]
for i in range(n):
    arr[i] = float(input())

for e, i in enumerate(arr):
    if i < 0:
        arr[e] *= -1


def QS(lst):
    if len(lst) < 2:
        return lst
    low, same, high = [], [], []
    pivot = lst[0]
    for item in lst:
        if item < pivot:
            low.append(item)
        if item == pivot:
            same.append(item)
        if item > pivot:
            high.append(item)
    return QS(low) + same + QS(high)


arr = QS(arr)
for i in range(0, n-1):
    if arr[i] == arr[i+1]:
        print(str(-arr[i]) + " " + str(arr[i]))


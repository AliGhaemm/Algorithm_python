import math


def merge_sort(arr, l, r):
    if r - l == 1:
        return
    mid = math.ceil((r + l) / 2)
    merge_sort(arr, l, mid)
    merge_sort(arr, mid, r)
    p1 = l
    p2 = mid
    b = []
    while p1 < mid or p2 < r:
        if p1 == mid:
            b.append(arr[p2])
            p2 += 1
        elif p2 == r:
            b.append(arr[p1])
            p1 += 1
        elif arr[p1] < arr[p2]:
            b.append(arr[p1])
            p1 += 1
        else:
            b.append(arr[p2])
            p2 += 1
    for i, j in enumerate(range(l, r)):
        arr[j] = b[i]


# arr = list(map(int, input().split()))
# print('not sorted array:')
# print(arr)
# merge_sort(arr, 0, len(arr))
# print('sorted array')
# print(arr)

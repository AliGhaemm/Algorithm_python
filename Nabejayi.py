import math

n = int(input())
lst = list(map(int, input().split()))


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


def inversion(a, l, r):
    if r - l <= 1:
        return 0
    mid = math.ceil((l+r)/2)
    result = 0
    result = result + inversion(a, l, mid)
    result = result + inversion(a, mid, r)
    k = 0
    for i in range(l, mid):
        while k < r-mid and a[i] > a[k+mid]:
            k += 1
        result += k
    merge_sort(a, l, mid)
    #merge_sort(a, mid, r)
    return result


print(inversion(lst, 0, len(lst)))

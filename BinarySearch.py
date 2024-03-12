import MergeSort


def binary_search(arr, b):
    MergeSort.merge_sort(arr, 0, len(arr))
    return binary_search_base(arr, 0, len(arr), b)


def binary_search_base(arr, l, r, a):
    if r - l <= 0:
        return False
    mid = (l+r) // 2
    if arr[mid] == a:
        return True
    elif arr[mid] > a:
        return binary_search_base(arr, l, mid, a)
    else:
        return binary_search_base(arr, mid, r, a)


arr = list(map(int, input().split()))
x = int(input())
print(binary_search(arr, x))

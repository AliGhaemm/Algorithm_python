from itertools import permutations


def isNabeja(jaygasht):
    count = 0
    l = len(jaygasht)
    for i in range(l - 1):
        for j in range(i+1, l):
            if jaygasht[i] > jaygasht[j]:
                count += 1
    return count


n, k = list(map(int, input().split()))
perm = permutations(range(1, n+1))
ans = 0
for current_perm in list(perm):
    if isNabeja(list(current_perm)) == k:
        ans += 1
print(ans)

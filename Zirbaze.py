n = int(input())
a = list(map(int, input().split()))

ans = float('-inf')
maxsum = a[0]
for i in range(1, n):
    maxsum = max(maxsum + a[i], a[i])
    ans = max(ans, maxsum)

print(ans)
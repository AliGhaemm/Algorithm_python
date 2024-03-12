n = int(input())
a = list(map(int, input().split()))
counter = [0 for _ in range(n)]
for i in a:
    counter[i-1] += 1
queue = []
for k, j in enumerate(counter):
    if j == 0:
        queue.append(k+1)
# print(counter)
# print(queue)


def push(b):
    queue.insert(0, b)


while len(queue) != 0:
    temp = queue.pop()
    counter[a[temp-1]-1] -= 1
    if counter[a[temp-1]-1] == 0:
        push(a[temp-1])

# print(counter)
out = []
for l in range(n):
    if counter[l] != 0:
        out.append(l+1)

print(len(out))
print(*out[:])

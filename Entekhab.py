q = int(int(input()))
n = [0]*q; r = [0]*q
for i in range(q):
    n[i], r[i] = list(map(int, input().split()))


def factorial(a):
    if a == 1 or a == 0:
        return 1
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
    return fact


def entekhab(k, l):
    return factorial(l) / (factorial(k) * factorial(l-k))


for i in range(q):
    print((entekhab(r[i], n[i])) % (7 + 10**9))

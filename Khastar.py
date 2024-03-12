n, q = list(map(int, input().split()))
query = [None for _ in range(q)]
for i in range(q):
    query[i] = list(map(int, input().split()))
people = [None for _ in range(n)]
for i in range(n):
    people[i] = {i + 1}


def query1(a,b):
    people[b - 1] = people[b - 1].union(people[a - 1])
    people[a - 1] = {}


def query2(c):
    print(len(people[c-1]))


def query3(d):
    return people[d-1]


for i in range(q):
    if query[i][0] == 1:
        query1(query[i][1]-1, query[i][2]-1)
    elif query[1][0] == 2:
        query2(query[i][1])
    else:
        print(query3(query[i][1]))

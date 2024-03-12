# import math
#
#
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n*factorial(n-1)
#
#
# def entekhab(k, n):
#     return int(factorial(n) / (factorial(k) * factorial(n-k)))
#
#
#
# final = []
# for number in questions:
#     ans = 0
#     test = number
#     number -= 1
#     for j in range(1, math.ceil(test / 2)):
#         ans += entekhab(j, test)
#         test -= 1
#     test = math.ceil((number-1) / 2)
#     for k in range(1, math.ceil(test / 2)):
#         ans += entekhab(k, test)
#         test -= 1
#     final.append(ans)
#
# for l in final:
#     print(l)


q = int(input())
questions = [0]*q
for i in range(q):
    questions[i] = int(input())

ajor = [0]*100000
ajor[0] = 1; ajor[1] = 1; ajor[2] = 2; ajor[3] = 3

for i in range(4, 100000):
    ajor[i] = ajor[i-1] + ajor[i-2] + ajor[i-3] - ajor[i-4]

for ques in questions:
    print((ajor[ques - 1]) % (7 + 10**9))

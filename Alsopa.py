def alsopa(x, n, a):
    num = pow(a, n)
    if num > x:
        return 0
    if num == x:
        return num
    return num + alsopa(x - num, n, a+1)


print(alsopa(10, 2, 1))

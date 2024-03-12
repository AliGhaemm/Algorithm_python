def is_valid(string):
    opn = 0
    close = 0
    for j in string:
        if j == '(':
            opn += 1
        else:
            close += 1
        if close > opn:
            return False
    if opn != close:
        return False
    return True


s = input()
stack = []
if is_valid(s):
    for i, k in enumerate(s):
        if k == '(':
            stack.append(i+1)
        else:
            print(stack.pop(), i+1)
else:
    print(-1)

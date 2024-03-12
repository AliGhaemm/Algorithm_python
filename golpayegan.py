x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))
x4 = 0
y4 = 0
z4 = 0
q4 = 0
try:
    slope12 = (y2 - y1) / (x2 - x1)
    slope23 = (y3 - y2) / (x3 - x2)
    slope31 = (y3 - y1) / (x3 - x1)
    if slope31 * slope23 == -1:
        x4 = x1 - x3 + x2
        y4 = y1 - y3 + y2
    elif slope12 * slope23 == -1:
        x4 = x1 - x2 + x3
        y4 = y1 - y2 + y3
    elif slope31 * slope12 == -1:
        x4 = x2 - x1 + x3
        y4 = y2 - y1 + y3
    print(x4, y4)
except ZeroDivisionError:
    if x1 == x2:
        x4=x3
    elif x1 == x3:
        x4=x2
    elif x3 == x2:
        x4=x1
    if y1==y2:
        y4=y3
    elif y1==y3:
        y4=y2
    elif y3==y2:
        y4=y1
    if (x4 + x3 + x2 + x1) == (y4 + y3 + y2 + y1):
        print(x4, y4)
    else:
        z4 = (-x3-x1-x2)
        q4 = (-y3-y1-y2)
        print(z4, q4)
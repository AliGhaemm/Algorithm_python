output = []
q = int(input())
# history = [0 for _ in range(q)]
s = list(input().split(' ')[2])
output.append(s)
for i in range(q-1):
    order_string = list(input().split(' '))
    temp = output[len(output)-1]
    if len(order_string) == 3:
        temp.insert(int(order_string[1]) - 1, order_string[2])
        output.append(temp)
        print('output is now: ', output)
        # print('history is now: ', history)
    elif len(order_string) == 2:
        output.remove(output[int(order_string[1]) - 1])
        output.append(temp)
        print('output is now: ', output)
        # print('history is now: ', history)
    else:
        output.pop()
        # output = history.pop()
        print('output is now: ', output)
        # print('history is now: ', history)

print('final output is:')
print(*output[:])

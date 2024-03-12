q = int(input())
orders = [None for _ in range(q)]
for i in range(q):
    orders[i] = input()
pointer = 0
output = []
for order in orders:
    if len(order.split(' ')) > 1:
        output.insert(pointer, order.split(' ')[1])
        pointer += 1
    else:
        if order == '-':
            if pointer != 0:
                pointer -= 1
        else:
            if pointer != q-1:
                pointer += 1
print(''.join(output))

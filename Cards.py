import math


def shuffle(card):
    length = int(len(card))
    first_deck = card[:math.floor(length/2)]
    second_deck = card[math.floor(length/2):]
    shuffled = []
    for i in range(math.floor(length/2)):
        shuffled.append(second_deck[i])
        shuffled.append(first_deck[i])
    if length%2 == 0:
        return shuffled
    else:
        shuffled.append(second_deck[math.ceil(length/2) - 1])
        return shuffled


cards = list(map(int, input().split()))
check_shuffle = shuffle(cards)
count = 1
while check_shuffle != cards:
    check_shuffle = shuffle(check_shuffle)
    count += 1
print(count)

from collections import Counter

f = open("input.txt", "r")
m = []
for line in f:
    m.append(line)


def getRank(s):
    count = Counter(s)
    for k in count:
        if count[k] == 5:
            return 6
    for k in count:
        if count[k] == 4:
            return 5
    if len(count) == 2:
        l = count.elements()
        first = l.__next__()
        if (count[first] in [2,3]):
            return 4
    for k in count:
        if count[k] == 3:
            return 3 
    pairs = 0
    for k in count:
        if count[k] == 2:
            pairs += 1
    if pairs == 2:
        return 2
    if pairs == 1:
        return 1
    return 0

def getTieBreakers(s):
    mapping = {
        "A":14,
        "K":13,
        "Q":12,
        "J":11,
        "T":10,
        "9":9,
        "8":8,
        "7":7,
        "6":6,
        "5":5,
        "4":4,
        "3":3,
        "2":2,
    }
    values = [] 
    for c in s:
        values.append(mapping[c])
    return values

allCards = []
for line in m:
    s = line.split()
    cards = s[0]
    bid = int(s[1])
    value = getRank(cards)
    remainderValue = getTieBreakers(cards)
    card = (value, *remainderValue, bid)
    allCards.append(card)
allCards.sort()
total = 0
for i, values in enumerate(allCards):
    b = values[-1]
    total += (b*(i+1))
print(total)
from collections import Counter

f = open("input.txt", "r")
m = []
for line in f:
    m.append(line)


def getRank(s, jokers):
    count = Counter(s)
    if (jokers == 5): return 6 
    for k in count:
        if count[k]+jokers == 5:
            return 6
    for k in count:
        if count[k]+jokers == 4:
            return 5
    if len(count) == 2:
        l = count.elements()
        first = l.__next__()
        if (count[first]+jokers in [2,3]):
            return 4
    for k in count:
        if count[k]+jokers == 3:
            return 3 
    pairs = 0
    jCounter = jokers
    for k in count:
        if count[k] == 2:
            pairs += 1
        elif count[k]+1 == 2 and jCounter > 0:
            pairs += 1
            jCounter -= 1
    if pairs == 2:
        return 2
    if pairs == 1:
        return 1
    return 0

def getRankWithJokers(s):
    return getRank(s.replace("J",""),s.count("J"))

def getTieBreakers(s):
    mapping = {
        "A":13,
        "K":12,
        "Q":11,
        "T":10,
        "9":9,
        "8":8,
        "7":7,
        "6":6,
        "5":5,
        "4":4,
        "3":3,
        "2":2,
        "J":1,
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
    value = getRankWithJokers(cards)
    remainderValue = getTieBreakers(cards)
    card = (value, *remainderValue, bid)
    allCards.append(card)

allCards.sort()
total = 0
for i, values in enumerate(allCards):
    b = values[-1]
    total += (b*(i+1))
print(total)


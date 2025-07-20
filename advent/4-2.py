f = open("input.txt","r")
m = []
for line in f:
    m.append(line)

cards = [1 for i in range(len(m))]
total = 0
index = 0 
for line in m:
    cardSplitter = line.split(":")
    n = int(cardSplitter[0].split()[1])
    numbers = cardSplitter[1].split("|")
    winners = numbers[0].split()
    winnerNumbs = set(int(s) for s in winners if s.isdigit())
    have = numbers[1].split()
    numbHave = [int(s) for s in have if s.isdigit()]
    o = 0
    for num in numbHave:
        if num in winnerNumbs:
            o += 1
    i = 0
    while i < o and index+i+1 < len(cards):
        cards[index+i+1] += cards[index]
        i+=1
    total += cards[index]
    index += 1
print(total)

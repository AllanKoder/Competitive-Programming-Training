f = open("input.txt","r")
m = []
for line in f:
    m.append(line)

total = 0
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
    if (o >0): total += 2**(o-1)

print(total)

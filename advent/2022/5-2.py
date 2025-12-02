f = open("input.txt","r")
levels = [[] for _ in range(7)]
level = -2
seeds = []
for line in f:
    if ":" in line:
        level += 1
    if line.startswith("seeds"):
        s = line.split()[1::]
        rangedSeeds = [int(n) for n in s]
        i = 0
        while i < len(rangedSeeds)-1:
            seeds.append((rangedSeeds[i], rangedSeeds[i] + rangedSeeds[i+1]))
            i+=2
    if len(line) > 0 and line[0].isdigit():
        stri = line.split()
        key = int(stri[1])
        rang = int(stri[2])
        dest = int(stri[0])
        levels[level].append((key,rang,dest))

def clamp(i, mi,ma):
    if i >= ma:
        return ma
    if i <= mi:
        return mi
    return i 

def getOverlap(s1,e1,s2,e2):
    if (e1 < s2): return None
    if (s1 > e2): return None
    return [clamp(s1, s2,e2),clamp(e1, s2,e2)]

def find_uncovered_ranges(start, end, ranges):
    if not ranges:
        return [(start, end)]
    uncovered = []
    ranges.sort()
    if ranges[0][0] > start:
        uncovered.append((start, ranges[0][0]))
    for i in range(len(ranges) - 1):
        if ranges[i][1] < ranges[i+1][0]:
            uncovered.append((ranges[i][1], ranges[i+1][0]))
    if ranges[-1][1] < end:
        uncovered.append((ranges[-1][1], end))
    return uncovered

def getOutput(s,e, ind):
    results = [] 
    covered = []
    for start, ran, desti in levels[ind]:
        result = getOverlap(s,e,start,start+ran)
        if (result):
            covered.append((result[0],result[1]))
            results.append((result[0]-start+desti, result[1]-start+desti))
    notCovered = find_uncovered_ranges(s,e, covered)
    return notCovered+results #change later

def location(seedRanges, ind):
    nextRanges = seedRanges
    nex = []
    for i in range(len(nextRanges)):
        s,e = seedRanges[i]
        nex += (getOutput(s,e, ind))

    if (ind >= 6):
        return min([asd[0] for asd in nex])
    return location(nex, ind+1)

print(seeds)
print(levels)
o = float("inf")
for s in seeds:
    o = min(location(seeds,0),o)
print(o)
f = open("input.txt", "r")

m = []
startCords = ()
y = 0
for line in f:
    m.append(line.replace("\n",""))
    for x in range(len(m[y])):
        if m[y][x] == "S":
            startCords = (y,x)
    y += 1

#run a BFS on all four directions, and get the min 

directions = [(0,1),(0,-1),(1,0),(-1,0)]

characterToDirection = {
"|": [(1,0),(-1,0)], #(y,x)
"-": [(0,1),(0,-1)],
"L": [(-1,0),(0,1)],
"7": [(1,0),(0,-1)],
"J": [(-1,0),(0,-1)],   
"F": [(1,0),(0,1)],
}

def addTuple(t1,t2):
    return tuple([t1[i]+t2[i] for i in range(len(t1))])

def getLetter(cords):
    return m[cords[0]][cords[1]]

ma = 0
for direction in directions: 
    count = 0
    start = addTuple(startCords, direction)
    visited = set()
    while getLetter(start) != "S":
        visited.add(start)
        if getLetter(start) == ".":
            break
        for nextDirection in characterToDirection.get(getLetter(start)):
            nextStep = addTuple(nextDirection, start)
            if nextStep not in visited:
                start = nextStep
                count += 1
                break
   
    ma = max(ma, (count+1)//2)

print(ma)
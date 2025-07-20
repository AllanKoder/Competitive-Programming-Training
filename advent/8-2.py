f = open("input.txt","r")
m = []
for line in f:
    m.append(line.replace("\n",""))

from collections import defaultdict
from collections import deque
import math

directions = m[0]

lefters = defaultdict(str)
righters = defaultdict(str)

starter = []
for i in range(2,len(m[2::])+2):
    line = m[i]
    splitter = line.split("=")
    head = splitter[0].replace(" ", "")
    leftRight = splitter[1].replace("(","").replace(")","").split(",")
    left = leftRight[0].replace(" ", "")
    right = leftRight[1].replace(" ", "")

    if head[-1] == "A":
        starter.append(head)
    lefters[head] = left
    righters[head] = right


AllSteps = []
for s in starter:
    steps = []
    queue = deque([(s,0)])
    directionIndex = 0 
    visited = set()
    while queue:
        element, step = queue.popleft()
        if element[-1] == "Z":
            steps.append(step)
        if (element,directionIndex) in visited:
            break
        visited.add((element,directionIndex))
        nextDirection = directions[directionIndex]
        directionIndex = (directionIndex+1)%len(directions) 
        nextElement = None
        if nextDirection == "L":
            nextElement = (lefters[element])
        else:
            nextElement = (righters[element])
        queue.append((nextElement, step+1))
    AllSteps.append(steps)
raw = [f[0] for f in AllSteps]
print(math.lcm(*raw))



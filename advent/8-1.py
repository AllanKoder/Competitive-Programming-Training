f = open("input.txt","r")
m = []
for line in f:
    m.append(line.replace("\n",""))

from collections import defaultdict
from collections import deque
import math

directions = m[0]
dir = defaultdict(set)
parent = defaultdict(set)
for i in range(2,len(m[2::])+2):
    line = m[i]
    splitter = line.split("=")
    head = splitter[0].replace(" ", "")
    leftRight = splitter[1].replace("(","").replace(")","").split(",")
    left = leftRight[0].replace(" ", "")
    right = leftRight[1].replace(" ", "")

    dir[head].add((left, right))
    parent[left].add(head)
    parent[right].add(head)


steps = 0
queue = deque([("ZZZ",0)])
visited = set()
while queue:
    element, step = queue.popleft()
    if element == "AAA":
        steps = step
        break
    if element in visited:
        continue
    visited.add(element)
    for nex in parent.get(element):
        queue.append((nex, step+1))
o = math.lcm(step, len(directions))
print(o)

#12083
f = open("input.txt","r")
m=[]
for line in f:
    li = [int(i) for i in line.split()]
#    li.reverse() for part 2
    m.append(li)

def getNext(line):
    base = True
    next = []
    for i in range(1,len(line)):
        v = line[i]-line[i-1]
        next.append(v)
        if line[i-1] != 0 or line[i] != 0:
            base = False
    if base:
        return 0
    wow = getNext(next)
    return line[-1]+wow
o = 0
for line in m:
    o += getNext(line)
print(o)

#1778564162
#1757008019
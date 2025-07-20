f = open("input.txt","r")
m = []
for line in f:
    m.append(line.replace("\n",""))
print(m)
class Number():
    def __init__(self,x:str) -> None:
        self.number = x
    number = ""

n = {}

#check if valid gear
pos = [[-1,0],[-1,-1],[-1,1],[0,-1],[0,1],[1,0],[1,-1],[1,1]]
def search(x,y):
    addedNumbs = set()
    for addY,addX in pos:
        newY = y+addY
        newX = x+addX
        if not (newY < 0 or newY >= len(m) or newX < 0 or newX >= len(m[newY])): 
            numbClass = n.get((newY,newX))
            if numbClass != None:
                addedNumbs.add(numbClass)
    if len(addedNumbs) == 2:
        x,y = list(addedNumbs)
        return (int(x.number),int(y.number))
    return (0,0)

# put in numbs into map
for y in range(len(m)):
    number = Number("")
    valid = False
    for i in range(len(m[y])):
        c = m[y][i]  
        if c.isdigit():
            n[(y,i)] = number
            number.number += str(c)
        else:
            number = Number("")
            valid = False


#count
o=0
for y in range(len(m)):
    for x in range(len(m[y])):
        c = m[y][x]
        if c == "*":
            xO,yO = search(x,y)
            o += xO*yO

print(o)
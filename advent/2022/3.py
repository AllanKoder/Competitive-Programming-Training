f = open("input.txt","r")
m = []
for line in f:
    m.append(line.replace("\n",""))
print(m)
s = set(".0123456789")
pos = [[-1,0],[-1,-1],[-1,1],[0,-1],[0,1],[1,0],[1,-1],[1,1]]

def hasSymbol(y,x):
    for addY,addX in pos:
        newY = y+addY
        newX = x+addX
        if not (newY < 0 or newY >= len(m) or newX < 0 or newX >= len(m[newY])): 
            if m[newY][newX] not in s:
                return True
    return False
            
o = 0
numbers = []
for y in range(len(m)):
    number = ""
    valid = False
    for i in range(len(m[y])):
        c = m[y][i]  
        if c.isdigit():
            if hasSymbol(y,i):
                valid = True
            number += str(c)
        else:
            if number != "" and valid: numbers.append(number)
            number = ""
            valid = False
    if number != "" and valid: numbers.append(number)

for number in numbers:
    o += int(number)
    print(number,o)
print(o)

#BAD: 527364

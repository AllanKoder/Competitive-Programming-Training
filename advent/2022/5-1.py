f = open("input.txt","r")
levels = [[] for _ in range(7)]
level = -2
seeds = []
for line in f:
    if ":" in line:
        level += 1
    if line.startswith("seeds"):
        s = line.split()[1::]
        seeds = [int(n) for n in s]
    if len(line) > 0 and line[0].isdigit():
        stri = line.split()
        key = int(stri[1])
        range = int(stri[2])
        dest = int(stri[0])
        levels[level].append((key,range,dest))

def location(input, ind):
    base = False
    if ind >=6:
        base = True
    output = input 
    for key,rang,dest in levels[ind]:
        if (input >= key and input < key + rang):
            output = input-key+dest
    
    if base:
        return output
    else:
        return location(output,ind+1)


o = float("inf")
for s in seeds:
    o = min(location(s,0),o)
print(o)
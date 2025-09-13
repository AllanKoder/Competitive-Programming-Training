t = int(input())

def compress(s):
    output = []

    index = 0
    while index < len(s):
        counter = 0
        char = s[index]
        while index < len(s) and s[index] == char:
            counter += 1
            index += 1
        output.append((char, counter))

    return output

def solve(matching, heard):
    
    ma = (compress(matching))
    he = (compress(heard))

    if len(ma) != len(he):
        return False
    
    for i in range(len(ma)):
        if ma[i][0] != he[i][0]:
            return False
        if he[i][1] > ma[i][1]*2 or he[i][1] < ma[i][1]:
            return False

    return True
for _ in range(t):
    matching = input()
    heard = input()

    print("YES" if solve(matching, heard) else "NO")
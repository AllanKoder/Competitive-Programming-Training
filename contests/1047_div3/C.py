t = int(input())
def solve(a,b):
    options = []

    if (a + b) % 2 == 0:
        options.append(a + b)
    
    if (a*b + 1) % 2 == 0:
        options.append(a*b + 1)

    if (b % 2 == 0 and (a * (b // 2) + 2) % 2 == 0):
        options.append(a*(b//2) + 2)
    
    if len(options) == 0:
        return -1
    else:
        return max(options)


for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a,b))

"""
Mistakes made:
- I tried to think of the scenerios when a number would be the max, and fixated on the scenerio of evens * odds
- Not seperating scrap from notable insights

Takeaways:
- Try to keep it simplier
- You don't need to check for scenerios to reach a certain answer, but just try to reach the answer and enumerate all the possibile answers
    - it is much easier that way


"""
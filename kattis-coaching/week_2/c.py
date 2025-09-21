result = 0
n = int(input())
s = input()
s = s.split()
for i in range(1, n // 2 + 1):
    good = False
    for j in range(i*2 - 1, n, i):
        if (int(s[j]) > int(s[j-i])):
            good = True
        else:
            good = False
            break
    if (good == True):
        result = i
        break
if (result == 0 or result > n // 2):
    print("ABORT!")
else:
    print(result)
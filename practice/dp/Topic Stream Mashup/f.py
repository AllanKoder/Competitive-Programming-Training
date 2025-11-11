import math

n, k = map(int, input().split())

derange = [0]*(k+1)
derange[0] = 1
derange[1] = 0
for i in range(2, k+1):
    derange[i] = (i-1)*(derange[i-1] + derange[i-2])


total = 0
for i in range(k+1):
    total += math.comb(n, i) * derange[i]
print(total)
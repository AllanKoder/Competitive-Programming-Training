a = list(input())
b = list(input())

movement1 = 0
movement2 = 0
unknowns = 0
for i in range(len(a)):
    if a[i] == "+":
        movement1 += 1
    elif a[i] == "-":
        movement1 -= 1

    if b[i] == "+":
        movement2 += 1
    elif b[i] == "-":
        movement2 -= 1
    else:
        unknowns += 1

diff = abs(movement2 - movement1)

import math
def get_arrangements(a, b):
    return math.factorial(a+b)/(math.factorial(a)*math.factorial(b))

def get_possibility():
    if movement1 == movement2 and unknowns == 0:
        return 1
    if diff > unknowns:
        return 0

    total_possible = 0
    valid_possible = 0
    for positives in range(0, unknowns+1):
        negatives = unknowns - positives
        if (positives - negatives + movement2) == movement1:
            valid_possible += get_arrangements(positives, negatives)
        total_possible += get_arrangements(positives, negatives)
    return valid_possible/total_possible

print(get_possibility())





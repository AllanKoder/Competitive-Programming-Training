from collections import defaultdict
t = int(input())


def construct_ideal_bin(ones_d, max_leng, bins):
    output = []
    # print(ones_d, max_leng)
    for i in range(max_leng):
        # If tied, does not matter
        should_be_one = bins - ones_d[i] 
        should_be_zero = ones_d[i]
        if should_be_one == should_be_zero:
            output.append(None)
        elif should_be_one > should_be_zero:
            output.append('1')
        else:
            output.append('0')
    return list(reversed(output))

def find_best_bin(bins, ideal_bin):
    scores = defaultdict(int)
    # Go reveresed direction

    for b in bins:
        for i in range(len(b)):
            reversed_i = len(b) - i - 1
            ideal_bit = ideal_bin[-(i+1)]

            if ideal_bit == None:
                continue

            comparing_bit = b[reversed_i]
            # print(comparing_bit, ideal_bit)
            if comparing_bit == ideal_bit:
                scores[b] += (10**(i+1)//10)
    # print(scores)

    best_bin = bins[0]
    best_score = -float('inf')
    for k,v in scores.items():
        if v > best_score:
            best_bin = k
            best_score = v
    return int(best_bin,2)

def summing(arr,selected):
    total = 0
    for a in arr:
        total += a^selected
    return total

def solve(arr):
    ones_d = defaultdict(int)
    max_bin_length = 0
    bins = []
    for v in arr:
        b = bin(v)[2:]
        bins.append(b)
        max_bin_length = max(max_bin_length, len(b))
        for i in range(0, 31):
            if (v & (2**i)) != 0:
                ones_d[i] += 1    

    ideal_bin = construct_ideal_bin(ones_d, max_bin_length, len(arr))
    # print("HERE")
    # print(ideal_bin)
    best_bin = find_best_bin(bins, ideal_bin)

    # print("best", best_bin)
    
    return summing(arr, best_bin)

for _ in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(solve(arr))


"""

Takeaway:

- Try to do mass operations
- Don't focus on the complex things, on your ideas, look back on the good parts and simplify on it. 
- Focus on the math on paper. Paper is the key
- To understand how to improve speed: note what the bottlenecks are, improve it.
- Never use bin(), just use the powers of 2. It is much faster to do so. And use the bitwise & to check.
"""
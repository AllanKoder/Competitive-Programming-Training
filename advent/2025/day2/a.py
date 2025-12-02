a = input()

def is_repeated(num):
    string = str(num)
    half = len(string)//2
    return string[:half] == string[half:]

total = 0
ids = a.split(",")
for id in ids:
    first,last = id.split("-")
    first = int(first)
    last = int(last)

    for i in range(first, last+1):
        if is_repeated(i):
            total += i

print(total)

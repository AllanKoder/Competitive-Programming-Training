f = open("input.txt", "r")
m = []
for line in f:
    m.append(line.replace("\n",""))

times = [int(i) for i in m[0].split(" ")[1::] if i != ""]
distances = [int(i) for i in m[1].split(" ")[1::] if i != ""]
print(times)
print(distances)
o = 1
for i in range(len(times)):
    totalTime = times[i]
    counter = 0
    for t in range(1,totalTime):
        speed = t
        leftOverTime = (times[i]-t)
        raceDistance = speed*leftOverTime
        if (raceDistance > distances[i]):
            counter += 1
    if counter > 0:
        o *= counter
print(o)
from pathlib import Path

def voronoiVillages(villageList):
    distances = [None] * len(villageList)
    minDistance = -1;

    for x in range(0, len(villageList)):
        if x == 0 or x == len(villageList) - 1:
            continue
        else:
            distances[x] = distanceRight(x, villageList) + distanceLeft(x, villageList)

        if distances[x] is not None and (minDistance == -1 or distances[x] < minDistance):
            minDistance = distances[x]

    return minDistance

def distanceRight(x, list):
    return (list[x + 1] - list[x]) / 2

def distanceLeft(x, list):
    return (list[x] - list[x - 1]) / 2

inputFile = open("windows_data\\s1\\s1.15.in", 'r')
numVillages = inputFile.readline()
villages = []
for line in inputFile:
    villages.append(int(line))
inputFile.close()

villages.sort()
print(voronoiVillages(villages))

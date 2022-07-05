A = [[1, 3], [2, 2], [3, 1]]
B = 4

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1])
    boxTypes.reverse()
    i = 0
    mx = 0
    while truckSize > 0 and i < len(boxTypes):
        if boxTypes[i][0] <= truckSize:
            mx += boxTypes[i][0] * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
        else:
            mx += truckSize * boxTypes[i][1]
            truckSize = 0
        i += 1
    return mx

print(maximumUnits(A, B))

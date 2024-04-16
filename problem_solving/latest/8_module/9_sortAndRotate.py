def checkMinUnknownPoint(nList: list, listSize: int) -> int:
    ascFlag = False
    descFlag = False
    for x in range(listSize-1):
        if (nList[x] - nList[x+1]) < 0:
            ascFlag = True
        elif (nList[x] - nList[x+1]) > 0:
            descFlag = True
        if ascFlag == descFlag:
            return nList[x] if (nList[x] < nList[x+1]) else nList[x+1]
    return nList[0] if ascFlag else nList[listSize-1]


listSize = int(input())
nList = [int(x) for x in input().split()]
print(checkMinUnknownPoint(nList, listSize))
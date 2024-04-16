def checkConsecutive(nList: list, size: int) -> str:
    minNum = nList[0]
    for x in nList:
        if x < minNum:
            minNum = x
    visitedList = [None] * size
    for x in nList:
        if (x - minNum) < size:
            visitedList[x-minNum] = True
    for x in visitedList:
        if not x:
            return "Not Consecutive"
    return "Consecutive"


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
print(checkConsecutive(nList, sizeOfList))

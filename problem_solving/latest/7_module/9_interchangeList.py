def interchangeList(numList: list, indexList: list, size: int) -> None:
    newNumList = [None] * size
    newIndexList = [None] * size
    for x in range(size):
        newNumList[indexList[x]] = numList[x]
        newIndexList[indexList[x]] = indexList[x]
    for x in newNumList:
        print(x, end="  ")
    print()
    for x in newIndexList:
        print(x, end="  ")


listSize = int(input())
nList = [int(x) for x in input().split()]
iList = [int(x) for x in input().split()]
interchangeList(nList, iList, listSize)


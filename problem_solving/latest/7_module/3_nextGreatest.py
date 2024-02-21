def findLargest(numL, start):
    listLen = len(numL)
    if start == listLen: return -1
    largest = numL[start]
    for x in range(start, listLen):
        if numL[x] > largest:
            largest = numL[x]
    return largest


def findNextGreatest(numList: list) -> None:
    for idx, x in enumerate(numList):
        numList[idx] = findLargest(numList, idx+1)


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
findNextGreatest(nList)
for x in nList:
    print(x, end=" ")


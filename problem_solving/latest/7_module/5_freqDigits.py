def sortFrequency(numList: list) -> None:
    freqList = [0] * 10
    numListLen = len(numList)
    for x in numList:
        freqList[x] += 1
    sortList = [0] * numListLen
    for idx, elm in enumerate(freqList):
        if elm > 0:
            if sortList[elm]:
                sortList[elm].append(idx)
            else:
                sortList[elm] = [idx]
    print(freqList)
    print(sortList)
    for idx in range(numListLen-1, 0, -1):
        if sortList[idx]:
            for elm in sortList[idx]:
                for idx_i in range(idx):
                    print(elm, end=" ")


listSize = int(input())
nList = [int(x) for x in input().split()]
sortFrequency(nList)


def findPeak(nList: list, size: int) -> None:
    for idx, value in enumerate(nList):
        left = nList[idx - 1] if (idx > 0) else (nList[idx] - 1)
        right = nList[idx + 1] if (idx < (size-1)) else (nList[idx] - 1)
        if left <= value >= right:
            print(value)


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
findPeak(nList, sizeOfList)
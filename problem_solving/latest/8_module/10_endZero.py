def zerosToEnd(numList: list, size: int) -> None:
    left = 0
    right = 1
    for idx in range(size-1):
        if numList[left] == 0 and numList[right] != 0:
            temp = numList[left]
            numList[left] = numList[right]
            numList[right] = temp
        elif numList[left] == 0:
            left -= 1
        left += 1
        right += 1


listSize = int(input())
nList = [int(x) for x in input().split()]
zerosToEnd(nList, listSize)
for x in nList:
    print(x, end=" ")
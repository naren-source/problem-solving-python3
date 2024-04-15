def sideMultiply(numList: list, size: int) -> None:
    temp = -1
    for idx in range(size):
        left = temp if 0 <= (idx-1) else numList[idx]
        right = numList[idx+1] if (idx+1) < size else numList[idx]
        temp = numList[idx]
        numList[idx] = left * right


listSize = int(input())
nList = [int(x) for x in input().split()]
sideMultiply(nList, listSize)
for x in nList:
    print(x, end=" ")

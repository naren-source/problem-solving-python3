def indexValShift(numList: list) -> None:
    temp = 0
    for idx, x in enumerate(numList):
        orgVal = numList[idx]
        indexVal = idx

sizeOfList = int(input())
nList = [int(x) for x in input().split()]
indexValShift(nList)
for x in nList:
    print(x, end=" ")

def checkRepeaters(numList: list, size: int) -> str:
    hashList = [0] * (size+2)
    repeaters = []
    for x in numList:
        hashList[x-1] += 1
    for idx, val in enumerate(hashList):
        if val > 1:
            repeaters.append(idx+1)
    return f"{repeaters[0]},{repeaters[1]}"


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
print(checkRepeaters(nList, sizeOfList))

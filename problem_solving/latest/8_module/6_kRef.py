def findRepeats(nList: list, n: int, k: int) -> int:
    hashList= [0] * k
    for x in nList:
        hashList[x] += 1
    maxRepeat = -1
    maxPos = -1
    for hIdx, hVal in enumerate(hashList):
            if hVal > maxRepeat:
                maxRepeat = hVal
                maxPos = hIdx
    return maxPos


n, k = input().split()
nList = [int(x) for x in input().split()]
print(findRepeats(nList, int(n), int(k)))
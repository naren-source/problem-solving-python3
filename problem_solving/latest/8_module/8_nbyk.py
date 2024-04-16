def findnByK(nList: list, n: int, k: int) -> None:
    hashList= [0] * n
    for x in nList:
        hashList[x] += 1
    nByK = []
    for hIdx in range(n):
        if hashList[hIdx] > int((n / k)):
            nByK.append(hIdx)
    for nIdx, nVal in enumerate(nByK):
        if nIdx == (len(nByK) - 1):
            print(nVal)
        else:
            print(nVal, end=",")


n, k = input().split()
nList = [int(x) for x in input().split()]
findnByK(nList, int(n), int(k))
def sortList(nList: list) -> list:
    for idx_i, i in enumerate(nList):
        for idx_j, j in enumerate(nList):
            if (idx_j < (len(nList) - idx_i - 1)) and (nList[idx_j] >= nList[idx_j + 1]):
                temp = nList[idx_j]
                nList[idx_j] = nList[idx_j+1]
                nList[idx_j+1] = temp
    return nList


def shiftRight(nL: list, start: int, end: int) -> list:
    for xx in range(end-1, start, -1):
        nL[xx] = nL[xx-1]
    return nL


def alternateSorting(nList: list, listSize: int) -> list:
    for idx in range(listSize - 1):
        if idx % 2 == 0:
            temp = nList[listSize-1]
            shiftRight(nList, idx, listSize)
            nList[idx] = temp
    return nList


size = int(input())
numList = [int(x) for x in input().split()]
numList = sortList(numList)
numList = alternateSorting(numList, size)
for x in numList:
    print(x, end=" ")


# Alternate sorting: Given an array of integers, rearrange the array in such a way that the first element is first maximum and second element is first minimum. Input : {1, 2, 3, 4, 5, 6, 7} Output : {7, 1, 6, 2, 5, 3, 4}
#
# Input Format
#
# Input denotes the size and the elements
#
# Constraints
#
# NIL
#
# Output Format
#
# print the altered array
#
# Sample Input 0
#
# 7
# 1 2 3 4 5 6 7
# Sample Output 0
#
# 7 1 6 2 5 3 4

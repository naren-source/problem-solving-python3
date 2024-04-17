def swapPos(swapList: list, pos1: int, pos2: int) -> None:
    temp = swapList[pos1]
    swapList[pos1] = swapList[pos2]
    swapList[pos2] = temp


def placeLargestInMiddle(nL: list, left: int, middle: int, right: int) -> None:
    if not (nL[middle]>nL[left] and nL[middle]>nL[right]):
        if nL[left] > nL[right]:
            swapPos(nL, left, middle)
        else:
            swapPos(nL, right, middle)


def zigZag(numList: list, size: int) -> None:
    for idx in range(1, size, 2):
        l = (idx-1) if (idx-1)>=0 else idx
        m = idx
        r = idx+1 if (idx+1)<=(size-1) else idx
        placeLargestInMiddle(numList, l, m, r)


listSize = int(input())
nList = [int(x) for x in input().split()]
zigZag(nList, listSize)
for x in nList:
    print(x, end=" ")


# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.
#
# Input Format
#
# Input contains the no of elements & array values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the altered array
#
# Sample Input 0
#
# 7
# 4 3 7 8 6 2 1
# Sample Output 0
#
# 3 7 4 8 2 6 1

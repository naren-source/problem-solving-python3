def checkMinUnknownPoint(nList: list, listSize: int) -> int:
    ascFlag = False
    descFlag = False
    for x in range(listSize-1):
        if (nList[x] - nList[x+1]) < 0:
            ascFlag = True
        elif (nList[x] - nList[x+1]) > 0:
            descFlag = True
        if ascFlag == descFlag:
            return nList[x] if (nList[x] < nList[x+1]) else nList[x+1]
    return nList[0] if ascFlag else nList[listSize-1]


listSize = int(input())
nList = [int(x) for x in input().split()]
print(checkMinUnknownPoint(nList, listSize))

# A sorted array is rotated at some unknown point, find the minimum element in it.
#
# Following solution assumes that all elements are distinct.
#
# Examples
#
# Input: {5, 6, 1, 2, 3, 4} Output: 1
#
# Input: {1, 2, 3, 4} Output: 1
#
# Input: {2, 1} Output: 1
#
# Input Format
#
# Input contains size and the values
#
# Constraints
#
# NIL
#
# Output Format
#
# Print the minimum element
#
# Sample Input 0
#
# 6
# 5 6 1 2 3 4
# Sample Output 0
#
# 1

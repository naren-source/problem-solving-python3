def interchangeList(numList: list, indexList: list, size: int) -> None:
    newNumList = [None] * size
    newIndexList = [None] * size
    for x in range(size):
        newNumList[indexList[x]] = numList[x]
        newIndexList[indexList[x]] = indexList[x]
    for x in newNumList:
        print(x, end="  ")
    print()
    for x in newIndexList:
        print(x, end="  ")


listSize = int(input())
nList = [int(x) for x in input().split()]
iList = [int(x) for x in input().split()]
interchangeList(nList, iList, listSize)

# Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according to given index array.
#
# Input Format
#
# First line contains the no of elements for array second line contains the array valuies & index arrray values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the altered array and the ordered index array. use tab for space
#
# Sample Input 0
#
# 3
# 10    11    12
# 1    0    2
# Sample Output 0
#
# 11    10    12
# 0    1    2

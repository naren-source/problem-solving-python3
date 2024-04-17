def findLargest(numL, start):
    listLen = len(numL)
    if start == listLen: return -1
    largest = numL[start]
    for x in range(start, listLen):
        if numL[x] > largest:
            largest = numL[x]
    return largest


def findNextGreatest(numList: list) -> None:
    for idx, x in enumerate(numList):
        numList[idx] = findLargest(numList, idx+1)


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
findNextGreatest(nList)
for x in nList:
    print(x, end=" ")

# Given an array of integers, replace every element with the next greatest element (greatest element on the right side) in the array. Since there is no element next to the last element, replace it with -1. For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
#
# Input Format
#
# Input contains the arraysize & values
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
# 18
# 26 75 37 29 8 -67 31 42 72 57 -89 45 32 61 -64 25  48 -94
# Sample Output 0
#
# 75 72 72 72 72 72 72 72 61 61 61 61 61 48 48 48 -94 -1

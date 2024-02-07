def rightShift(nList: list, startIndex: int) -> None:
    index = len(nList) - startIndex
    for x in range(index):
        nList[len(nList)-1-x] = nList[len(nList)-1-x-1]


def insertIntoList(nList: list, n: int) -> None:
    nList += [None]
    for idx, x in enumerate(nList):
        if x and n <= x:
            rightShift(nList, idx)
            nList[idx] = n
            break
    if not nList[len(nList)-1]:
        nList[len(nList)-1] = n


listSize = int(input())
numList = [int(x) for x in input().split()]
insertNum = int(input())
insertIntoList(numList, insertNum)
for x in numList:
    print(x, end=" ")

#
# Write a program to insert an element in the array
#
# Input Format
#
# Input will be the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 10
# 1 5 18 28 33 39 47 73 77 84
# 37
# Sample Output 0
#
# 1 5 18 28 33 37 39 47 73 77 84

def shiftRight(nList: list, start: int, end: int) -> None:
    for x in range(end-start):
        nList[end-x] = nList[end-x-1]


def replaceAndShift(nList: list, ins: int, zPos: int, count: int) -> list:
    for idx, x in enumerate(nList):
        if idx > ins and x < 0:
            shiftRight(nList, ins, idx)
            zPos += 1
            count += 1
            return [x, zPos, count]
    return [nList[ins], zPos, count]


def listSegregation(nList: list) -> None:
    zeroPos = -1
    count = -1
    for idx, x in enumerate(nList):
        if x == 0:
            zeroPos = idx
        elif x > 0:
            nList[idx], zeroPos, count = replaceAndShift(nList, idx, zeroPos, count)
    shiftRight(nList, count+1, zeroPos)
    nList[count+1] = 0


sizeOfArr = int(input())
numList = [int(x) for x in input().split()]
listSegregation(numList)
for x in numList:
    print(x, end=" ")


# Given an array that has positive numbers and negative numbers and zero in it. You need to separate the negative numbers and positive numbers in such a way that negative numbers lies to left of zero and positive numbers to the right and the original order of elements should be maintained.
#
# Input Format
#
# Each line contains the array size & values
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
# 5
# 98 -54 122 87 0
# Sample Output 0
#
# -54 0 98 122 87

# 9 -1 8 -2 -3 7 0 6 5 -4

# -1 -2 9 8 -3 7 0 6 5
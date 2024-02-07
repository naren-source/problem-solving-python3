def findSecMax(nList: list) -> int:
    max = -1
    sMax = -2
    for x in nList:
        if x >= max:
            sMax = max
            max = x
        elif x > sMax:
            sMax = x
    return sMax


sizeOfArr = int(input())
numList = [int(x) for x in input().split()]
print(findSecMax(numList))


# Find 2nd maximum element in a given array in one iteration.
#
# Input Format
#
# Each line contains the array size & values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# only one traversal
#
# Output Format
#
# print the second max
#
# Sample Input 0
#
# 5
# 98 -54 122 87 0
# Sample Output 0
#
# 98
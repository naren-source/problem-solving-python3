def bubbleSort(nList: list) -> None:
    for idx_i, i in enumerate(nList):
        for idx_j, j in enumerate(nList):
            if (idx_j < (len(nList) - idx_i - 1)) and (nList[idx_j] >= nList[idx_j + 1]):
                temp = nList[idx_j]
                nList[idx_j] = nList[idx_j+1]
                nList[idx_j+1] = temp


listSize = int(input())
numList = [int(x) for x in input().split()]
bubbleSort(numList)
for x in numList:
    print(x, end=" ")


# Write a program to implement a bubble sort
#
# Input Format
#
# Input is the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the sorted elements
#
# Sample Input 0
#
# 10
# 837 635 354 667 956 109  434 599 913  983
# Sample Output 0
#
# 109 354 434 599 635 667 837 913 956 983

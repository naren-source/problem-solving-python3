def sortFrequency(numList: list) -> None:
    freqList = [0] * 10
    numListLen = len(numList)
    for x in numList:
        freqList[x] += 1
    sortList = [0] * numListLen
    for idx, elm in enumerate(freqList):
        if elm > 0:
            if sortList[elm]:
                sortList[elm].append(idx)
            else:
                sortList[elm] = [idx]
    for idx in range(numListLen-1, 0, -1):
        if sortList[idx]:
            for elm in sortList[idx]:
                for idx_i in range(idx):
                    print(elm, end=" ")


listSize = int(input())
nList = [int(x) for x in input().split()]
sortFrequency(nList)

# Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
#
# Input Format
#
# Input contains the no of elements and array values
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
# 17
# 3 2 4 6 2 4 3 3 4 5 6 3 2 4 5 5 3
# Sample Output 0
#
# 3 3 3 3 3 4 4 4 4 2 2 2 5 5 5 6 6

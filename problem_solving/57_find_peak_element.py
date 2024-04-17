def findPeak(nList: list, size: int) -> None:
    for idx, value in enumerate(nList):
        left = nList[idx - 1] if (idx > 0) else (nList[idx] - 1)
        right = nList[idx + 1] if (idx < (size-1)) else (nList[idx] - 1)
        if left <= value >= right:
            print(value)


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
findPeak(nList, sizeOfList)

# Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. For example, for input array {5, 10, 20, 15}, 20 is the only peak element. For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. Note that we need to return all the unique peak elements.
#
# Following corner cases give better idea about the problem. 1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}. 2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}. 3) If all elements of input array are same, every element is a peak element.
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
# Print the peak element
#
# Sample Input 0
#
# 4
# 5 10 20 15
# Sample Output 0
#
# 20
# Sample Input 1
#
# 7
# 10 20 15 2 23 90 67
# Sample Output 1
#
# 20
# 90

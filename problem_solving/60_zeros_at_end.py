def zerosToEnd(numList: list, size: int) -> None:
    left = 0
    right = 1
    for idx in range(size-1):
        if numList[left] == 0 and numList[right] != 0:
            temp = numList[left]
            numList[left] = numList[right]
            numList[right] = temp
        elif numList[left] == 0:
            left -= 1
        left += 1
        right += 1


listSize = int(input())
nList = [int(x) for x in input().split()]
zerosToEnd(nList, listSize)
for x in nList:
    print(x, end=" ")


# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
#
# Input Format
#
# Input contains the size and values
#
# Constraints
#
# NIL
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 11
# 1 9 8 4 0 0 2 7 0 6 0
# Sample Output 0
#
# 1 9 8 4 2 7 6 0 0 0 0

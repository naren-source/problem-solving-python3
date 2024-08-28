def checkConsecutive(nList: list, size: int) -> str:
    minNum = nList[0]
    for x in nList:
        if x < minNum:
            minNum = x
    visitedList = [None] * size
    for x in nList:
        if (x - minNum) < size:
            visitedList[x-minNum] = True
    for x in visitedList:
        if not x:
            return "Not Consecutive"
    return "Consecutive"


sizeOfList = int(input())
nList = [int(x) for x in input().split()]
print(checkConsecutive(nList, sizeOfList))


# Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.
#
# Examples: a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.
#
# b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.
#
# c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.
#
# d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.
#
# Input Format
#
# Input contains the no of elements and the elements
#
# Constraints
#
# Dynamic memory allocation
#
# Output Format
#
# Print Consecutive if the function returns true else print Not Consecutive
#
# Sample Input 0
#
# 5
# 5 2 3 1 4
# Sample Output 0
#
# Consecutive
# Sample Input 1
#
# 5
# 34 23 52 12 3
# Sample Output 1
#
# Not Consecutive

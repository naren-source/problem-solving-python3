def swapList(numList: list, start: int, stop: int) -> None:
    temp = numList[start]
    numList[start] = numList[stop]
    numList[stop] = temp


def reverseList(numList: list) -> None:
    listLen = len(numList)
    for x in range(int(listLen/2)):
        swapList(numList, x, listLen-x-1)


size = int(input())
listOfNum = [int(x) for x in input().split()]
reverseList(listOfNum)
for x in listOfNum:
    print(x, end=" ")




# Write a program to reverse the given array
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
# 825 573 380 192 150 691 219 353 2 6
# Sample Output 0
#
# 6 2 353 219 691 150 192 380 573 825

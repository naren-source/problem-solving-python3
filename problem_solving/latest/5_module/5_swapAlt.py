def swapPair(nList: list, position) -> None:
    temp = nList[position]
    nList[position] = nList[position+1]
    nList[position+1] = temp


def swapAlternate(nList: list) -> None:
    for idx, n in enumerate(nList):
        if idx % 2 == 0 and idx < (len(nList)-1):
            swapPair(nList, idx)


sizeOfList = int(input())
numList = [int(x) for x in input().split()]
swapAlternate(numList)
for x in numList:
    print(x, end=" ")



# Swap Alternate Elements Write a program to swap alternate elements in an array
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
# 15
# 83 51 75 47 67 72 2 86 22 82 4 86 19 50 35
# Sample Output 0
#
# 51 83 47 75 72 67 86 2 82 22 86 4 50 19 35


def sumOfArray(nList: list) -> int:
    sum = 0
    for x in nList:
        sum += x
    return sum


def replaceWithSum(nList: list) -> None:
    sumOfList = sumOfArray(nList)
    for idx, x in enumerate(nList):
        nList[idx] = sumOfList - x


sizeOfArr = int(input())
numList = [int(x) for x in input().split()]
replaceWithSum(numList)
for x in numList:
    print(x, end=" ")


# Write a program to replace every element with sum of all other elements
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
# print the array
#
# Sample Input 0
#
# 5
# 12 34 56 76 87
# Sample Output 0
#
# 253 231 209 189 178
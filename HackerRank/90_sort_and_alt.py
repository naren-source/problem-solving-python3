def sortAndAlter(numList: list, size: int) -> None:
    for x in range(size):
        for y in range(size - 1 - x):
            if numList[y] > numList[y+1]:
                temp = numList[y]
                numList[y] = numList[y+1]
                numList[y+1] = temp
    for idx, val in enumerate(numList):
        if idx % 2 == 0:
            print(val, end=" ")


listSize = int(input())
nlist = [int(x) for x in input().split()]
sortAndAlter(nlist, listSize)


# Write a program to sort numbers in a array and print the numbers with alternate digits. Ip: {4,2,5,3,7} Op: {2,4,7}
#
# Input Format
#
# Input contains the array size and the value
#
# Constraints
#
# 1 ≤ array_size ≤ 1000
#
# Output Format
#
# print the alternate elments in a sorted order
#
# Sample Input 0
#
# 5
# 4 2 5 3 7
# Sample Output 0
#
# 2 4 7
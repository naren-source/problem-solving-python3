def evenOddSegregation(numList: list) -> None:
    left = -1
    right = -1
    for idx, val in enumerate(numList):
        if numList[idx] %2 == 0:
            left = idx
        elif numList[idx] %2 == 1 and right == -1:
            right = idx
        if left > right and (left > -1 and right > -1):
            temp = numList[right]
            numList[right] = numList[left]
            numList[left] = temp
            left = right
            right += 1


def rearrangeEvenAndOdd(arr, n):
    j = -1
    for i in range(0, n):
        if arr[i] % 2 == 0:
            j = j + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


listSize = int(input())
nList = [int(x) for x in input().split()]
# evenOddSegregation(nList)
rearrangeEvenAndOdd(nList, listSize)

for x in nList:
    print(x, end=" ")


# Given an array A[], write a 'C' program to segregates even and odd numbers. The ouput should have all even numbers first, and then odd numbers.
#
# Input Format
#
# Input contains the array values
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
# 7
# 12 34 45 9 8 90 3
# Sample Output 0
#
# 12 34 8 90 45 9 3

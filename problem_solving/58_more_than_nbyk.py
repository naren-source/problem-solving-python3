def findnByK(nList: list, n: int, k: int) -> None:
    hashList= [0] * n
    for x in nList:
        hashList[x] += 1
    nByK = []
    for hIdx in range(n):
        if hashList[hIdx] > int((n / k)):
            nByK.append(hIdx)
    for nIdx, nVal in enumerate(nByK):
        if nIdx == (len(nByK) - 1):
            print(nVal)
        else:
            print(nVal, end=",")


n, k = input().split()
nList = [int(x) for x in input().split()]
findnByK(nList, int(n), int(k))

# Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3.
#
# Input Format
#
# Input contains size n , k and the values
#
# Constraints
#
# NIL
#
# Output Format
#
# print the value else print No such element
#
# Sample Input 0
#
# 8 4
# 3 1 2 2 1 2 3 3
# Sample Output 0
#
# 2,3

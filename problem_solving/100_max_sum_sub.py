def findMaxSumSub(nList: list, size: int) -> None:
    left = 0
    right = left
    cSum = 0
    mSum = [-1] * 4

    while right < size:
        if nList[right] < 0:
            cSum = 0
            left = right + 1
            right = left
        else:
            cSum += nList[right]
            if cSum >= mSum[0]:
                if cSum == mSum[0]:
                    if (right-left) > mSum[1]:
                        mSum = cSum, right-left, left, right
                else:
                    mSum = cSum, right-left, left, right
            right += 1

    for x in range(mSum[2], mSum[3]+1):
        if x == mSum[2]:
            print('{', end="")
            print(nList[x], end=",")
        elif x == (mSum[3]):
            print(nList[x], end="} ")
        else:
            print(nList[x], end=",")
    print(mSum[0], end="")


listSize = int(input())
numList = [int(x) for x in input().split()]
findMaxSumSub(numList, listSize)





# You are given an array of integers, which has both positive and negative numbers. You are required to find the maximum sum of the subarray (positive integers only), if two arrays qualify, choose the array with more number of elements. Solve it in single navigation.
#
# I/P {9,1,2, -3, -4, 10, 5, -1, 9, 2, 3} O/P {10,5} 15
#
# Input Format
#
# First line denotes array size and the next line denotes the values
#
# Constraints
#
# NIL
#
# Output Format
#
# print the subarray and the sum {%d,%d..} %d
#
# Sample Input 0
#
# 11
# 9 1 2 -3 -4 10 5 -1 9 2 3
# Sample Output 0
#
# {10,5} 15

def checkLargestSubarray(nList: list, size) -> None:
    left, right = -1, -1
    for x in range(size-1):
        flag = 0
        if nList[x] == 1:
            flag += 1
        else:
            flag -= 1
        for y in range(x+1, size):
            if nList[y] == 1:
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                if (y - x) > (right - left):
                    left = x
                    right = y
    if left == right:
        print("No such array")
    else:
        print(f"{left}->{right}")


listSize = int(input())
nList = [int(x) for x in input().split()]
checkLargestSubarray(nList, listSize)

# Given an array containing only 0s and 1s, find the largest subarray which contain equal no of 0s and 1s. Examples:
#
# Input: arr[] = {1, 0, 1, 1, 1, 0, 0} Output: 1 to 6 (Starting and Ending indexes of output subarray)
#
# Input: arr[] = {1, 1, 1, 1} Output: No such array
#
# Input: arr[] = {0, 0, 1, 1, 0} Output: 0 to 3 Or 1 to 4
#
# Input Format
#
# Input contains the no of elements & array values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# Print the index i1->in if exist else print No such array . If more than 1 found print all
#
# Sample Input 0
#
# 7
# 1 0 1 1 1 0 0
# Sample Output 0
#
# 1->6

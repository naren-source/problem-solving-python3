def findRepeats(nList: list, n: int, k: int) -> int:
    hashList= [0] * k
    for x in nList:
        hashList[x] += 1
    maxRepeat = -1
    maxPos = -1
    for hIdx, hVal in enumerate(hashList):
            if hVal > maxRepeat:
                maxRepeat = hVal
                maxPos = hIdx
    return maxPos


n, k = input().split()
nList = [int(x) for x in input().split()]
print(findRepeats(nList, int(n), int(k)))

# Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n. Find the maximum repeating number in this array. For example, let k be 10 the given array be arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2. Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.
#
# Input Format
#
# Input contains size,k and the values
#
# Constraints
#
# Dyanmic memory
#
# Output Format
#
# Print the value
#
# Sample Input 0
#
# 14 10
# 1 2 2 2 0 2 0 2 3 8 0 9 2 3
# Sample Output 0
#
# 2

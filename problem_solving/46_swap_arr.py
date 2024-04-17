def swapList(numList: list, size: int) -> list:
    newList: list = [-1] * size
    for idx, val in enumerate(numList):
        newList[val] = idx
    return newList


#diff prob but similar
def swapList1(arr: list, n: int) -> list:
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n

    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)

    return arr


listSize = int(input())
nList = [int(x) for x in input().split()]
nList = swapList(nList, listSize)
for x in nList:
    print(x, end=" ")


# Given an array of size n where all elements are in range from 0 to n-1, change contents of arr[] so that arr[i] = j is changed to arr[j] = i.
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
# print the altered array
#
# Sample Input 0
#
# 4
# 1 3 0 2
# Sample Output 0
#
# 2 0 3 1
# Explanation 0
#
# Explanation for the above output. Since arr[0] is 1, arr[1] is changed to 0 Since arr[1] is 3, arr[3] is changed to 1 Since arr[2] is 0, arr[0] is changed to 2 Since arr[3] is 2, arr[2] is changed to 3

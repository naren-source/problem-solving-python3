def sideMultiply(numList: list, size: int) -> None:
    temp = -1
    for idx in range(size):
        left = temp if 0 <= (idx-1) else numList[idx]
        right = numList[idx+1] if (idx+1) < size else numList[idx]
        temp = numList[idx]
        numList[idx] = left * right


listSize = int(input())
nList = [int(x) for x in input().split()]
sideMultiply(nList, listSize)
for x in nList:
    print(x, end=" ")

# Given an array of integers, update every element with multiplication of previous and next elements with following exceptions. a) First element is replaced by multiplication of first and second. b) Last element is replaced by multiplication of last and second last.
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
# 5
# 2 3 4 5 6
# Sample Output 0
#
# 6 8 15 24 30
# Explanation 0
#
# // We get the above output using following // arr[] = {2*3, 2*4, 3*5, 4*6, 5*6}

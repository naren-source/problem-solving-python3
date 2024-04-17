def sumList(arr: list, pos: int) -> int:
    sum = 0
    for x in range(pos, len(arr)):
        sum += arr[x]
    return sum


def sumOfRight(arr: list) -> list:
    for i in range(len(arr)):
        arr[i] = sumList(arr, i+1)
    return arr


arrLen = int(input())
arrList = [int(x) for x in input().split(" ")]
result = sumOfRight(arrList)
for x in result:
    print(x, end=" ")


# Write a program to replace every element with sum of its right side elements
#
# Input Format
#
# Input will be the size and the values
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the altered array
#
# Sample Input 0
#
# 10
# 90 -60 78 12 76 61 -53 49 -6 -93
# Sample Output 0
#
# 64 124 46 34 -42 -103 -50 -99 -93 0

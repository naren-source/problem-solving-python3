def sumOfArray(arr: list) -> int:
    sum = 0
    # for x in range(len(arr)):
    #     sum += arr[x]
    for x in arr:
        sum += x
    return sum


arrLen = int(input())
arrList = [int(x) for x in input().split(" ")]
print(sumOfArray(arrList))


# Write a program to print the sum of the array
#
# Input Format
#
# Input will be the size of the array and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the sum
#
# Sample Input 0
#
# 10
# 90 -60 78 12 76 61 -53 49 -6 -93
# Sample Output 0
#
# 154

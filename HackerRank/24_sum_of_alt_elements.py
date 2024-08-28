def sumOfAltArray(arr: list) -> int:
    sum = 0
    for id_x, x in enumerate(arr):
        sum += x if id_x % 2 == 0 else 0
    return sum


arrLen = int(input())
arrList = [int(x) for x in input().split(" ")]
print(sumOfAltArray(arrList))


# Write a program to print the sum of alternate elements
#
# Input Format
#
# Input will be the size and the elements
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
# 825 573 380 192 150 691 219 353 2 6
# Sample Output 0
#
# 1576

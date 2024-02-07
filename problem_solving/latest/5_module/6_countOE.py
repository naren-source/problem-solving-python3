def countOddEven(nList: list) -> None:
    odd = 0
    even = 0
    for x in nList:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"{odd} {even}")



listSize = int(input())
numList = [int(x) for x in input().split()]
countOddEven(numList)


# Write a program to count the odd and even no of elements
#
# Input Format
#
# Input will have the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the odd count and then even count
#
# Sample Input 0
#
# 10
# 33 90 31 89 63 56 22 93 35 52
# Sample Output 0
#
# 6 4

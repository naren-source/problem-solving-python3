def findUnique(nList: list) -> int:
    count = 0
    for x in nList:
        for y in nList:
            if x == y:
                count += 1
        if count == 1:
            return x
        count = 0


listSize = int(input())
numList = [int(x) for x in input().split()]
print(findUnique(numList))


# Write a program to print the unique element in the array where every element will appear twice
#
# Input Format
#
# Input will have size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the unique element
#
# Sample Input 0
#
# 19
# 335 2 45 85 163 177 335 177 2 548 429 548 716 904 45 85 163 716 904
# Sample Output 0
#
# 429

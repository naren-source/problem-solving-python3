def notInNum(num: int, check: int) -> bool:
    while num:
        r = num % 10
        if r == check:
            return False
        num = int(num/10)
    return True


def removeDups(nList: list, size: int) -> int:
    n = 0
    for x in nList:
        if notInNum(n, x):
            n = n*10 + x
    return n


size = int(input())
numList = [int(x) for x in input().split()]
print(removeDups(numList, size))


# Write a  program to remove duplicates.
#
# I/P {1,2,2,3,4,4,4,3,2,3,1} O/P 1234
#
# Input Format
#
# Input will have the size and the values
#
# Constraints
#
# form an integer
#
# Output Format
#
# print the unique values as an integer
#
# Sample Input 0
#
# 11
# 1 2 2 3 4 4 4 3 2 3 1
# Sample Output 0
#
# 1234

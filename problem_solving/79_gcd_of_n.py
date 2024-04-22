def gcdOfN(nList: list) -> int:
    sNum = nList[0]
    for x in nList:
        if x < sNum:
            sNum = x
    # sNum = int(sNum/2) + 1
    while sNum > 0:
        flag = True
        for x in nList:
            if not x % sNum == 0:
                flag = False
                break
        if flag:
            return sNum
        sNum -= 1


testCase = int(input())
for tc in range(testCase):
    size, *nList = input().split()
    nList = [int(x) for x in nList]
    print(gcdOfN(nList))

# Write a program to find the GCD of N numbers
#
# Input Format
#
# First line denotes the number of test cases Next lines will have the no of elements and the values
#
# Constraints
#
# 1 ≤ noe ≤ 100000
#
# 1 ≤ values ≤ 100000000007
#
# Output Format
#
# print the GCD
#
# Sample Input 0
#
# 5
# 5 2 4 8 16 32
# 4 3 6 9 12
# 3 5 10 15
# 2 50 100
# 1 30
# Sample Output 0
#
# 2
# 3
# 5
# 50
# 30

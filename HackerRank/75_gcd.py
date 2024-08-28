def findGcd(num1: int, num2: int) -> int:
    sNum = num1 if num1 > num2 else num2
    for x in range(int((sNum/2)+1), 0, -1):
        if (num1 % x == 0) and (num2 % x == 0):
            return x


testCase = int(input())
for tc in range(testCase):
    n1, n2 = input().split()
    print(findGcd(int(n1), int(n2)))


# Write a program to find the GCD of two numbers
#
# Input Format
#
# First line denotes the test cases. Each test cases contain two integers separated by space
#
# Constraints
#
# 1 ≤ n1,n2 ≤ 105
#
# Output Format
#
# print the GCD of two numbers
#
# Sample Input 0
#
# 3
# 36 60
# 98 56
# 12345 5670
# Sample Output 0
#
# 12
# 14
# 15

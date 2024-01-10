def checkTwosPower(n: int) -> str:
    while n >= 1:
        if n == 2:
            return "YES"
        n /= 2
    return "NO"


inputs = int(input())
for i in range(inputs):
    n = int(input())
    print(checkTwosPower(n))


# Write a C program to receive a number and check whether it is two’s power or not? In mathematics, a power of two is a number of the form 2^n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent. ... Because two is the base of the binary numeral system, powers of two are common in computer science.
#
# Input Format
#
# First line specifies the number of test cases. Each line has an integer that needs
#
# to be processed by your program.
#
# Constraints
#
# 1 ≤ n1 ≤ 200000000
#
# Output Format
#
# Print YES OR NO
#
# Sample Input 0
#
# 3
# 512
# 4908
# 4096
# Sample Output 0
#
# YES
# NO
# YES

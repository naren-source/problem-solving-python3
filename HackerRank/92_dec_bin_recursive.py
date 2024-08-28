def convertDecToBin(n: int, pos) -> int:
    if not n:
        return 0
    result = (n % 10) * (2**pos)
    n = int(n/10)
    pos += 1
    return result + convertDecToBin(n, pos)


decNum = int(input())
print(convertDecToBin(decNum, 0))


# Write a program to find the decimal value of given number in the binary form - RECURSIVE
#
# I/P 100 O/P 4
#
# I/P 1111 O/P 15
#
# Input Format
#
# Given a binary number
#
# Constraints
#
# should apply recursive function
#
# Output Format
#
# print the decimal value
#
# Sample Input 0
#
# 100
# Sample Output 0
#
# 4

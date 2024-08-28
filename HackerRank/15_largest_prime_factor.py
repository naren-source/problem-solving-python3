def checkPrime(n: int) -> bool:
    for i in range(2, int((n/2))+1):
        if n % i == 0:
            return False
    return True


def largestPrimeFactor(n: int) -> int:
    for i in range(n, 2, -1):
        if (n % i == 0) and checkPrime(i):
            return i
    return 1


inputNum = int(input())
print(largestPrimeFactor(inputNum))



# Write a program to find the largest prime factor of a number
#
# Input Format
#
# Input contains an integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print the factor
#
# Sample Input 0
#
# 256987
# Sample Output 0
#
# 3253

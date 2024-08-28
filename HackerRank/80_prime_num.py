def checkPrime(n: int) -> str:
    for x in range(2, int((n+1)/2)):
        if n % x == 0:
            return "NOT PRIME"
    return "PRIME"


testCase = int(input())
while testCase:
    testCase -= 1
    print(checkPrime(int(input())))


# Write a Program to check whether the given number is prime or not..
#
# Input Format
#
# First line tells the number of test cases and the following lines contain the numbers to check for prime
#
# Constraints
#
# 2 ≤ num ≤ 1000000000000007
#
# Output Format
#
# Print PRIME or NOT PRIME
#
# Sample Input 0
#
# 5
# 9127
# 6856
# 8221
# 2354
# 5099
# Sample Output 0
#
# PRIME
# NOT PRIME
# PRIME
# NOT PRIME
# PRIME

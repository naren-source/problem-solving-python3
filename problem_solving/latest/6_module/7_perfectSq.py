def checkPerfSq(n: int) -> str:
    mainNum = n
    n = int(n/2) + 1
    for x in range(n):
        num = n - x
        if num*num == mainNum:
            return "YES"
    return "NO"


print(checkPerfSq(int(input())))

# Write a program to find whether a given number is a perfect square or not.
#
# Input Format
#
# Input contains the value to check for perfect
#
# Constraints
#
# The input can be large - max of 19 digits, so write an optimized solution, naive method of checking all possible values from 1 to n will not be accepted. Note : Do not use sqrt() function
#
# Output Format
#
# print YES or NO
#
# Sample Input 0
#
# 2500
# Sample Output 0
#
# YES
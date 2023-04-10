def check_perfect_sq(n: int) -> str:
    for i in range(n):
        if i*i == n:
            return "YES"
        elif i*i > n:
            return "NO"


print(check_perfect_sq(int(input())))


# =================================
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
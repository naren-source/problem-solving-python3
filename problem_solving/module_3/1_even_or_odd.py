def checkEvenOrOdd(number):
    # if number % 2 == 0:
    #     return "EVEN"
    # else:
    #     return "ODD"
    return "EVEN" if number % 2 == 0 else "ODD"


numberOfInputs = int(input())
for i in range(numberOfInputs):
    value = int(input())
    print(checkEvenOrOdd(value))


# ===================================================

# Write a C program to check the given number whether it is even or odd?
#
# Note : Do not use remainder operator or division operator
#
# Input Format
#
# The first line informs you the number of test cases. Every single line has an
#
# integer, that needs to checked whether it is even or odd
#
# Constraints
#
# -2147483647 ≤ n1 ≤ 2147483647
#
# Output Format
#
# print EVEN or ODD
#
# Sample Input 0
#
# 3
# 2
# 45
# 60
# Sample Output 0
#
# EVEN
# ODD
# EVEN

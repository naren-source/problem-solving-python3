def generateFibo(n: int) -> None:
    x = 0
    y = 1
    z = x + y
    for limit in range(n-1):
        print(z, end=" ")
        z = x + y
        x = y
        y = z


generateFibo(int(input()))


# Write a program to print the nth term of fibonacci series. n will be in the range of 0 - 50
#
# Input Format
#
# Input contains the value n
#
# Constraints
#
# 0 ≤ num ≤ 50
#
# Output Format
#
# print the series
#
# Sample Input 0
#
# 7
# Sample Output 0
#
# 1 1 2 3 5 8 13

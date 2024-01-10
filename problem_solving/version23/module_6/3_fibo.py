def fibonacci(n: int):
    first = 0
    second = 1
    fibo = first+second
    for i in range(n):
        print(fibo, end=" ")
        fibo = first + second
        first = second
        second = fibo


fibonacci(int(input()))



# ==============================================
#
# Write a 'C' program to print the nth term of fibonacci series. n will be in the range of 0 - 50
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
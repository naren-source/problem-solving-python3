def fact(n):
    if not n:
        return 1
    return n * fact(n-1)


def check_strong(n: int) -> str:
    sum_of_factorial = 0
    org_num = n
    while n:
        r = n % 10
        sum_of_factorial += fact(r)
        n = int(n / 10)
    return "STRONG" if sum_of_factorial == org_num else "NOT STRONG"


print(check_strong(int(input())))


#=============================================
# Write a 'C' program to check whether the given number is strong number or not. Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Input : n = 145 Output : Yes Sum of digit factorials = 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Input Format
#
# Integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print STRONG or NOT STRONG
#
# Sample Input 0
#
# 145
# Sample Output 0
#
# STRONG

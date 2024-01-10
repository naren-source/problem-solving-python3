def is_prime(n: int) -> bool:
    number = n
    n -= 1
    while n > 1:
        if number % n == 0:
            return False
        n -= 1
    return True


def largest_prime_factor(n: int) -> int:
    check_num = int(n/2) + 1
    while check_num > 1:
        if (n % check_num == 0) and is_prime(check_num):
            return check_num
        check_num -= 1
    return 0


print(largest_prime_factor(int(input())))



# =============================================================
# Write a 'C' program to find the largest prime factor of a number
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

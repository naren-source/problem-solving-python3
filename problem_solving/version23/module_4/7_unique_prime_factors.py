def is_prime(n: int) -> bool:
    number = n
    n -= 1
    while n > 1:
        if number % n == 0:
            return False
        n -= 1
    return True


def unique_prime_factor(n: int) -> int:
    count = 0
    check_num = int(n/2) + 1
    while check_num > 1:
        if (n % check_num == 0) and is_prime(check_num):
            count += 1
        check_num -= 1
    return count


print(unique_prime_factor(int(input())))


# ============================================================
# Write a 'C' program to count the unique prime factors of the number
#
# Input Format
#
# Input represents the number
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print the count
#
# Sample Input 0
#
# 12
# Sample Output 0
#
# 2

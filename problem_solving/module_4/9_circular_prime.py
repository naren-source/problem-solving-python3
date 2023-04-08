def pow_and_count(n: int) -> list:
    pwr = 1
    count = 0
    while n:
        pwr *= 10
        count += 1
        n = int(n/10)
    return [int(pwr / 10), count]


def circulate(n: int) -> int:
    return ((n % 10 * pow_and_count(n)[0]) + int(n / 10)) if n > 9 else n


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def circular_prime(start: int, end: int):
    for i in range(start, end+1):
        number = i
        prime = True
        count = pow_and_count(number)[1]
        while count:
            if not is_prime(number):
                prime = False
                break
            number = circulate(number)
            count -= 1
        print(i, end=" ") if prime else None


start_num, end_num = input().split()
circular_prime(int(start_num), int(end_num))
# =============================================================================
# Write a program to generate the circular prime numbers in the given range.
# EX: 1193, 1931, 9311 and 3119 are all prime
#
# Input Format
#
# Input represent the start and end
#
# Constraints
#
# 1 ≤ start,end ≤ 100000000
#
# Output Format
#
# print the values
#
# Sample Input 0
#
# 10 50
# Sample Output 0
#
# 11 13 17 31 37

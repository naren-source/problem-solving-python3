def arrange_digits(n: int, order: int) -> int:
    even_grp = 0
    odd_grp = 0
    e_pwr = 1
    o_pwr = 1
    while n:
        r = n % 10
        if r % 2 != 0:
            odd_grp += r * o_pwr
            o_pwr *= 10
        else:
            even_grp += r * e_pwr
            e_pwr *= 10
        n = int(n/10)
    return (even_grp * o_pwr) + odd_grp if order else (odd_grp * e_pwr) + even_grp


arrange_type, number = input().split()
print(arrange_digits(int(number), int(arrange_type)))


# ================================================================
# Write a 'C' program to arrange the even digits first and odd digits second of the given number vice versa.
#
# Input Format
#
# First input is option and next the value If the option is 0 - odd digits first 1 - even digits first
#
# Constraints
#
# 1 ≤ num ≤ 100000007
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 0 89745
# Sample Output 0
#
# 97584

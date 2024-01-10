def count_digits(n: int) -> int:
    if not n:
        return 0
    return 1 + count_digits(int(n / 10))


def swap_num(n: int) -> int:
    return ((n % 10) * 10) + int(n / 10)


def swap_alternate(n: int) -> int:
    swapped = 0
    extra = 0
    swap_pwr = 1
    if count_digits(n) % 2 != 0:
        extra = n % 10
        n = int(n / 10)
    while n:
        r = n % 100
        swapped += swap_num(r) * swap_pwr
        swap_pwr *= 100
        n = int(n/100)
    return ((swapped * 10) + extra) if extra else swapped


print(swap_alternate(int(input())))


# ============================================
# Write a 'C' program to swap the alternate digits of the given number
#
# Input Format
#
# input will have an integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# Print the value
#
# Sample Input 0
#
# 54687
# Sample Output 0
#
# 45867

def check_factors(n: int) -> int:
    count = 0
    for i in range(n):
        if i > 1 and i != n and n % i == 0:
            count += 1
    return count


def n_factors(n: int) -> int:
    num = n
    while True:
        n += 1
        if check_factors(n) > num:
            return n


print(n_factors(int(input())))


# ======================================================
# Write a 'C' program to find the first number that has more than 'n' factors.Excluding 1 and that number
#
# Input Format
#
# Input contains n
#
# Constraints
#
# n - will be in the range 2 to 200.
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 12
# Explanation 0
#
# 2,3,4,6
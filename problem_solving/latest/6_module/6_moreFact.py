def findFactors(n: int) -> int:
    count = 0
    for x in range(2,n):
        if n % x == 0:
            count += 1
    return count


def nFactors(n: int) -> int:
    number = 0
    while True:
        factors = findFactors(number)
        if factors > n:
            return number
        number += 1


print(nFactors(int(input())))


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
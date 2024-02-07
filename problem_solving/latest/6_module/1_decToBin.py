def decToBinConvert(n: int) -> int:
    power = 1
    binNum = 0
    while n:
        r = n % 2
        binNum = binNum + r*power
        power *= 1
        n = int(n / 2)
    return binNum


print(decToBinConvert(int(input())))


# Write a 'C' program to convert decimal number into binary number
#
# Input Format
#
# Input contains the value to convert
#
# Constraints
#
# -2147483647 ≤ num ≤ 2147483647
#
# Output Format
#
# print the values in binary format
#
# Sample Input 0
#
# 12
# Sample Output 0
#
# 1100

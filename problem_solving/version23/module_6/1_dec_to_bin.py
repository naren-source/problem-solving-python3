def dec_bin(dec: int) -> int:
    bin = 0
    pwr = 1
    while dec != 0:
        r = dec % 2
        bin = bin + (r * pwr)
        pwr *= 10
        dec = int(dec / 2)
    return int(bin)


print(dec_bin(int(input())))



# =========================================
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
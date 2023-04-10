def dec_hex(dec: int) -> str:
    hex_map = ['A', 'B', 'C', 'D', 'E', 'F']
    hex = ""
    while dec != 0:
        r = dec % 16
        if r>9:
            r = hex_map[r-10]
        else:
            r = str(r)
        hex = r + hex
        dec = int(dec / 16)
    return hex


print(dec_hex(int(input())))

# =============================================
# Write a 'C' program to convert the decimal values into hexa decimal
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
# print the values in hexa decimal format
#
# Sample Input 0
#
# 7648000
# Sample Output 0
#
# 74B300
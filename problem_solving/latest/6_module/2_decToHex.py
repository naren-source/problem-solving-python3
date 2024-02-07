def decToHexConvert(n: int) -> str:
    hexList = ['A', 'B', 'C', 'D', 'E', 'F']
    hexNum = ""
    while n:
        r = n % 16
        r = str(r) if r <= 9 else hexList[r-10]
        hexNum =  r + hexNum
        n = int(n / 16)

    return hexNum


print(decToHexConvert(int(input())))


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

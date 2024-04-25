def findLen(n: int) -> int:
    count = 0
    while n:
        count += 1
        n = int(n/10)
    return count


def leftToRightAdd(n1: int, n2: int) -> str:
    len1 = findLen(n1)
    len2 = findLen(n2)
    length = len1 if len1>len2 else len2
    sum = 0
    carry = 0
    zeroFlag = False

    while length > 0:

        first = int(n1 / (10**(len1-1)))
        n1 = n1 % (10**(len1-1))

        second = int(n2 / (10 ** (len2 - 1)))
        n2 = n2 % (10 ** (len2 - 1))

        add = first + second + carry
        sum = (sum * 10) + (add % 10)
        carry = int(add / 10)

        if sum == 0 and carry > 0:
            zeroFlag = True

        length -= 1
        len1 -= 1
        len2 -= 1

    if carry > 0:
        sum = (sum*10) + carry

    return f"{sum}" if not zeroFlag else f"0{sum}"


num1 = int(input())
num2 = int(input())
print(leftToRightAdd(num1, num2))


# Given two numbers, perform addition from Left->Right
#
# 6321
#
# 5235
# 1656
# Input Format
#
# Get the two integers
#
# Constraints
#
# 1 ≤ n1,n2 ≤ 1000000007
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 1234
# 5678
# Sample Output 0
#
# 68031
# Sample Input 1
#
# 5239744
# 52348
# Sample Output 1
#
# 0563654
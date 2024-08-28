def findLen(n: int) -> int:
    count = 0
    while n:
        count += 1
        n = int(n/10)
    return count


def findCircular(n1: int, n2: int) -> str:
    num = n2
    nLen = findLen(n2)
    while num:
        r = n2 % 10
        m = int(n2/10)
        power = 10 ** (nLen-1)
        n2 = (r * power) + m
        if n2 == n1:
            return "YES"
        num = int(num/2)
    return "NO"


num1 = int(input())
num2 = int(input())
print(findCircular(num1, num2))


# Find if the second input is a circular number of the first input
#
# Input Format
#
# Input will have two values n1 and n2
#
# Constraints
#
# 1 ≤ n1,n2 ≤ 1000000000
#
# Output Format
#
# print YES or NO
#
# Sample Input 0
#
# 12345
# 45123
# Sample Output 0
#
# YES
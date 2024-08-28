def findLen(n: int) -> int:
    count = 0
    while n:
        count += 1
        n = int(n/10)
    return count


def baseAdditions(n1: int, n2: int, base: int) -> int:
    n1size = findLen(n1)
    n2size = findLen(n2)
    num = n1 if n1size > n2size else n2
    sum = ""
    carry = 0
    power = 1
    while num:
        add = (n1 % 10) + (n2 % 10) + carry
        sum = f"{add % base}{sum}"
        carry = int(add / base)
        power *= 10
        n1 = int(n1/10)
        n2 = int(n2/10)
        num = int(num/10)
    if carry > 0:
        sum = f"{carry}{sum}"
    return int(sum)


num1, num2, base = input().split()
print(baseAdditions(int(num1), int(num2), int(base)))


# Write a function long add_any_Base(int num1, int num2, int base)
#
# I/P 123, 231, 4 O/P 1020
#
# I/P 7561, 3062, 8 O/P 12643
#
# Input Format
#
# Input will have three integers n1,n2,base
#
# Constraints
#
# 1 ≤ num1,num2 ≤ 1000000
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 123 231 4
# Sample Output 0
#
# 1020

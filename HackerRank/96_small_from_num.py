def formNum(number: int, insert: int) -> int:
    storeNum = number
    checkNum = number
    while checkNum:
        if checkNum % 10 == insert:
            return number
        checkNum = int(checkNum/10)

    right = 0
    power = 1
    while number:
        rem = number % 10
        if insert > rem:
            return (((number*10)+insert)*power) + right
        right += rem*power
        number = int(number / 10)
        power *= 10

    return (insert*power) + storeNum


def formSmallest(n: int) -> int:
    num = 0
    while n:
        r = n % 10
        n = int(n/10)
        num = formNum(num, r)
    return num


print(formSmallest(int(input())))


# Form the smallest number from the input number I/P: 991233612 O/P 12369
#
# Input Format
#
# Given a number
#
# Constraints
#
# Should not use arrays
#
# Output Format
#
# print the smallest number
#
# Sample Input 0
#
# 991233612
# Sample Output 0
#
# 12369
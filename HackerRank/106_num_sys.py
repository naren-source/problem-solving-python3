def isAllowed(num: int) -> bool:
    allowedNums = [3, 4]
    while num:
        r = num % 10
        if not (r in allowedNums):
            return False
        num = int(num / 10)
    return True


def formNumSys(n: int) -> int:
    number = 0
    while n:
        number += 1
        if isAllowed(number):
            n -= 1

    return number


print(formNumSys(int(input())))



# Form a number system with only 3 and 4. Find the nth number of the number system. Eg.) The numbers are: 3, 4, 33, 34, 43, 44, 333, 334, 343, 344, 433, 434, 443, 444, 3333, 3334, 3343, 3344, 3433, 3434, 3443, 3444 ….] I/P : 10 O/P : 344
#
# Input Format
#
# Input is an integer
#
# Constraints
#
# NIL
#
# Output Format
#
# print the value
#
# Sample Input 0
#
# 10
# Sample Output 0
#
# 344

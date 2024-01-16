def reverseNum(n: int) -> int:
    reverse = 0
    while n:
        last = n % 10
        reverse = reverse*10 + last
        n = int(n/10)
    return reverse


def calcSq(n: int) -> int:
    return n*n


def checkAdam(num: int) -> str:
    return "ADAM" if calcSq(num) == reverseNum(calcSq(reverseNum(num))) \
        else "NOT ADAM"


print(checkAdam(int(input())))


# Write a 'C' program to check whether the given number is an adam number or not. Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other. Input : 12 Output : Adam Number Explanation: Square of 12 = 144 Reverse of 12 = 21 Square of 21 = 441 Now Square of 12 and square of reverse of 12 are reverse of each other. Therefore 12 is Adam number.
#
# Input Format
#
# Given a number
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print ADAM or NOT ADAM
#
# Sample Input 0
#
# 12
# Sample Output 0
#
# ADAM

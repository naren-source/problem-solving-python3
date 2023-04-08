def reverse_of(n: int) -> int:
    reverse = 0
    while n:
        r = n % 10
        reverse = (reverse * 10) + r
        n = int(n / 10)
    return reverse


def square_of(n: int) -> int:
    return n*n


def check_adam(n: int) -> str:
    return "ADAM" if \
        square_of(n) == reverse_of(square_of(reverse_of(n))) \
        else "NOT ADAM"


print(check_adam(int(input())))


# =====================================================
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

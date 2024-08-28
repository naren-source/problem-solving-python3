def divide_num(dividend: int, divisor: int) -> None:
    quotient = int(dividend / divisor)
    remainder = dividend % divisor
    print(f"{dividend} / {divisor} = {quotient}")
    print(f"{dividend} % {divisor} = {remainder}")


for _ in range(int(input())):
    dividend, divisor = [int(i) for i in input().split()]
    divide_num(dividend, divisor)



# Division is one of the basic arithmetic operations; each part of a division equation has a name. The three main names are the dividend, the divisor, and the quotient.
#
# a. Dividend - The dividend is the number you are dividing up b. Divisor - The divisor is the number you are dividing by c. Quotient - The quotient is the answer d. Remainder – The left over after the division, the group that is incomplete Dividend ÷ Divisor = Quotient + Remainder
#
# Write a program to divide two numbers, print the quotient and remainder – without the division operation ?
#
# Input Format
#
# First line specifies the number of test cases. Every single line has two numbers
#
# for the program to process.
#
# Constraints
#
# 1≤ n1 ≤ 2,147,483,647
#
# Output Format
#
# %d / %d = %d %d % %d = %d
#
# Sample Input 0
#
# 3
# 12 5
# 90 5
# 1048576 65536
# Sample Output 0
#
# 12 / 5 = 2
# 12 % 5 = 2
# 90 / 5 = 18
# 90 % 5 = 0
# 1048576 / 65536 = 16
# 1048576 % 65536 = 0

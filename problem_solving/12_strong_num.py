def calcFact(num: int) -> int:
    if num == 1:
        return 1
    return num * calcFact(num-1)


def checkStrong(num: int) -> str:
    sumOfFact = 0
    storedNum = num
    while num:
        last = num % 10
        sumOfFact += calcFact(last)
        num = int(num/10)

    return "STRONG" if sumOfFact == storedNum else "NOT STRONG"


print(checkStrong(int(input())))



# Write a  program to check whether the given number is strong number or not. Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Input : n = 145 Output : Yes Sum of digit factorials = 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Input Format
#
# Integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print STRONG or NOT STRONG
#
# Sample Input 0
#
# 145
# Sample Output 0
#
# STRONG

def swap(n: int) -> int:
    return n


def noOfDigits(n: int) -> int:
    count = 0
    while n:
        count += 1
        n = int(n/10)
    return count


def swapDigits(n: int) -> int:
    q = int(n / 10)
    r = n % 10
    return (r*10 + q) if q>0 else r


def swap_alternate(n: int) -> int:
    result = 0
    while n:
        digitsOfN = noOfDigits(n)
        firstTwoDigits = int(n / int(10 ** (digitsOfN - 2))) if digitsOfN > 1 else n
        result = (result * (10 ** noOfDigits(firstTwoDigits))) + swapDigits(firstTwoDigits)
        n = int(n % int(10 ** (digitsOfN- 2))) if digitsOfN > 1 else 0
    return result


inputNumber = int(input())
print(swap_alternate(inputNumber))


# Write a 'C' program to swap the alternate digits of the given number
#
# Input Format
#
# input will have an integer
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# Print the value
#
# Sample Input 0
#
# 54687
# Sample Output 0
#
# 45867

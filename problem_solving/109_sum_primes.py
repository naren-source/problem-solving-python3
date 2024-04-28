def addIfPrime(num: int) -> int:
    for x in range(2, num):
        if num % x == 0:
            return 0
    return num


def sumPrimes(n: int) -> int:
    primeSum = 0
    while n > 1:
        r = n % 10
        primeSum += addIfPrime(r)
        n = int(n/10)
    return primeSum


print(sumPrimes(int(input())))

# Write a program to calculate sum of primes present as digits of given number N. Ex: i/p: 333 o/p: 9
#
# Input Format
#
# Input contains an integer
#
# Constraints
#
# 2 ≤ N ≤ 50000
#
# Output Format
#
# Print sum of primes in the digit
#
# Sample Input 0
#
# 333
# Sample Output 0
#
# 9

def checkPrime(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def rotateNum(n: int) -> int:
    r = n % 10
    n = int(n / 10)
    return (r*(10**countDigits(n))) + n


def countDigits(n: int) -> int:
    count = 0
    while n > 0:
        n = int(n/10)
        count += 1
    return count


def generateCircularPrime(sNum: int, eNum: int) -> None:
    for i in range(sNum, eNum+1):
        n = i
        noOfDigits = countDigits(n)
        isPrime = True
        for _ in range(noOfDigits):
            n = rotateNum(n)
            if not checkPrime(n):
                isPrime = False
                break
        if (countDigits(n) == noOfDigits) and isPrime:
            print(i, end=" ")


start, end = input().split(' ')
generateCircularPrime(int(start), int(end))


# Write a  program to generate the circular prime numbers in the given range. EX: 1193, 1931, 9311 and 3119 are all prime
#
# Input Format
#
# Input represent the start and end
#
# Constraints
#
# 1 ≤ start,end ≤ 100000000
#
# Output Format
#
# print the values
#
# Sample Input 0
#
# 10 50
# Sample Output 0
#
# 11 13 17 31 37

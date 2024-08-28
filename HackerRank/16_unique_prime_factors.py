def checkPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def checkUniquePrimeFactors(n: int) -> int:
    prevNum = 1
    count = 0
    for i in range(2, n+1):
        if n < 2:
            break
        if n % i == 0 and checkPrime(i):
            n = int(n/i)
            if i != prevNum:
                prevNum = i
                count += 1
            i -= 1
    return count


num = int(input())
print(checkUniquePrimeFactors(num))


# Write a program to count the unique prime factors of the number
#
# Input Format
#
# Input represents the number
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print the count
#
# Sample Input 0
#
# 12
# Sample Output 0
#
# 2

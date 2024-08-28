def isPrime(num: int) -> bool:
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def checkTwoPrimes(n: int) -> str:
    start = 2
    end = n - start
    while start < end:
        if isPrime(start) and isPrime(end):
            return f"{start} {end}"
        start += 1
        end -= 1


print(checkTwoPrimes(int(input())))

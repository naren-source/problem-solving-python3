def fibonacci_naive(n):
    x = 0
    y = 1
    result = None
    for i in range(2, (n+1)):
        result = x + y
        x = y
        y = result
    return result


def fibonacci_recursive(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_tabulation(n):
    fiboTable = [0] * (n+1)
    fiboTable[1] = 1
    for fibo in range(2, n+1):
        fiboTable[fibo] = fiboTable[fibo-1] + fiboTable[fibo-2]
    return fiboTable[n]


def fibonacci_memoization(n, memo=None):
    if not memo:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 1:
        return 1
    if n == 0:
        return 0

    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]


print(fibonacci_naive(10))
print(fibonacci_recursive(10))
print(fibonacci_tabulation(10))
print(fibonacci_memoization(10))

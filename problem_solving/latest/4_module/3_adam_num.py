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

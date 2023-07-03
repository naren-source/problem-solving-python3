def checkTwosPower(n: int)->str:
    if n % 2 != 0 or n < 2:
        return "NO"
    if n == 2:
        return "YES"
    return checkTwosPower(int(n / 2))


times = int(input())
result = [None]*3
for i in range(times):
    n = int(input())
    result[i] = checkTwosPower(n)


for i in result:
    print(i)




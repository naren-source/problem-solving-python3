def generatePattern(n: int) -> None:
    count = 0
    for x in range(1, n+1):
        for y in range(x):
            count += 1
            print(count, end="")
            print("*", end="") if not (y == x - 1) else None
        print()
    for x in range(n, 0, -1):
        count -= x
        newCount = count
        for y in range(x):
            newCount += 1
            print(newCount, end="")
            print("*", end="") if not (y == x - 1) else None
        print()


generatePattern(int(input()))


# Obtain a output as follows:
# N=5
# 1
# 2*3
# 4*5*6
# 7*8*9*10
# 11*12*13*14*15
# 11*12*13*14*15
# 7*8*9*10
# 4*5*6
# 2*3
# 1
#
# Input Format
#
# Input contains the value N
#
# Constraints
#
# 1 ≤ N ≤ 10
#
# Output Format
#
# print the pattern
#
# Sample Input 0
#
# 5
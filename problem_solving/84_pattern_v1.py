def printPattern(n: int) -> None:
    counter = 1
    for x in range(1, n+1):
        for y in range(x):
            print(counter, end="")
            print("*", end="") if not (y == x-1) else None
            if x % 2 == 0:
                counter -= 1
            else:
                counter += 1
        counter += x if not (x % 2 == 0) else (x+1)
        print()


printPattern(int(input()))


# Write a program to print the pattern.
# For n=5
# 1
# 3*2
# 4*5*6
# 10*9*8*7
# 11*12*13*14*15
#
# Input Format
#
# Input contains n
#
# Constraints
#
# NIL
#
# Output Format
#
# print the pattern
#
# Sample Input 0
#
# 5
# Sample Output 0
#
# 1
# 3*2
# 4*5*6
# 10*9*8*7
# 11*12*13*14*15
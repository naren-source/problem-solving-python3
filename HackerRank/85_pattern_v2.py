def printPattern(n: int) -> None:
    for v in range(1, n+1):
        for h in range(n+1):
            value = v
            if v % 2 == 0:
                if h == 0 :
                    value += 1
            else:
                if h == n:
                    value += 1
            print(value, end=" ")
        print()


printPattern(int(input()))


# Write a program to print the pattern
# for n=3
# 1 1 1 2
# 3 2 2 2
# 3 3 3 4
# n=6; n stands for number of lines
# 1111112
# 3222222
# 3333334
# 5444444
# 5555556
# 7666666
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
# Print the pattern
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 1112
# 3222
# 3334
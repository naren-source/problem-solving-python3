def formPattern(n: int) -> None:
    for x in range(1, n+1):
        counter = 0
        cSum = 0
        spaceStr = "\t" * (n-x)
        print(spaceStr, end="")
        for y in range(1, x+1):
            if counter == 0:
                cSum += x
                print(cSum, end="")
            else:
                cSum += (n - counter)
                print("\t\t", end="")
                print(cSum, end="")
            counter += 1
        print()


formPattern(int(input()))

# write a program to print the pattern.
# For n=5
#
#                 1
#             2       6
#         3       7       10
#     4       8       11      13
# 5       9       12      14      15
# Input Format
#
# Given n
#
# Constraints
#
# nil
#
# Output Format
#
# use tab for space
#
# Sample Input 0
#
# 5
# Sample Output 0
#
#                 1
#             2        6
#         3        7        10
#     4        8        11        13
# 5        9        12        14        15





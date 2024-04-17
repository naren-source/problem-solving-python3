def generateDiagonal(matrixList: list, r: int, c: int) -> None:
    colShift = 0
    rowShift = 0
    while rowShift < r:
        for cIdx in range(colShift, rowShift+colShift+1):
            if cIdx < c:
                print(matrixList[rowShift+colShift-cIdx][cIdx], end="       ")
        print()

        if colShift == (c-1):
            break

        if not (rowShift == r-1):
            rowShift += 1
        else:
            colShift += 1


row, col = input().split()
matrix = [[None] * int(col)] * int(row)
for x in range(int(row)):
    matrix[x] = [int(c) for c in input().split()]
generateDiagonal(matrix, int(row), int(col))


# Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.
#
#  1     2     3     4
#  5     6     7     8
#  9    10    11    12
# 13    14    15    16
# 17    18    19    20
# Diagonal printing of the above matrix is
#
# 1
# 5   2
# 9   6   3
# 13  10  7   4
# 17  14  11  8
# 18  15  12
# 19  16
# 20
# Input Format
#
# Input contains rowCount, columnCount and the values
#
# Constraints
#
# Dynamic memory allocation
#
# Output Format
#
# Print the values
#
# Sample Input 0
#
# 5 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 17 18 19 20
# Sample Output 0
#
# 1
# 5    2
# 9    6    3
# 13    10    7    4
# 17    14    11    8
# 18    15    12
# 19    16
# 20

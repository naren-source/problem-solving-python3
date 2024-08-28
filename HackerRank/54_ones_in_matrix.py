def checkMaxOnes(matrixList: list, r: int, c: int) -> int:
    rowWithMaxOnes = -1
    maxOnes = -1
    for xRowIdx, xRowVal in enumerate(matrixList):
        zeroPos = -1
        for xColIdx, xColVal in enumerate(xRowVal):
            if xColVal == 0:
                zeroPos = xColIdx
                break
        currentRowOnes = c - (zeroPos + 1)
        if currentRowOnes > maxOnes:
            maxOnes = currentRowOnes
            rowWithMaxOnes = xRowIdx
    return rowWithMaxOnes


row, col = input().split()
matrix = [[None] * int(col)] * int(row)
for r in range(int(row)):
    matrix[r] = [int(c) for c in input().split()]
print(checkMaxOnes(matrix, int(row), int(col)))


# Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
#
# Example
# Input matrix
# 0 1 1 1
# 0 0 1 1
# 1 1 1 1 // this row has maximum 1s
# 0 0 0 0
#
# Output: 2
#
# Input Format
#
# Input contains rowCount,columnCount and the values
#
# Constraints
#
# Dynamic memory allocation
#
# Output Format
#
# print the row value
#
# Sample Input 0
#
# 4 4
# 0 1 1 1
# 0 0 1 1
# 1 1 1 1
# 0 0 0 0
# Sample Output 0
#
# 2

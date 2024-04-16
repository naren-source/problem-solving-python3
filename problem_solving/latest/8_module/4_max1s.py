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
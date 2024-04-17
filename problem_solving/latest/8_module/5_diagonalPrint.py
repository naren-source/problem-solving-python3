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

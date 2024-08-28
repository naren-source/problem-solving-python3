def transposeMatrix(matrixx: list, r: int, c: int) -> list:
    tMatrix = [None] * c
    for idx, val in enumerate(tMatrix):
        tMatrix[idx] = [None] * r

    for cIdx in range(c):
        for rIdx in range(r):
                tMatrix[cIdx][rIdx] = matrixx[rIdx][cIdx]
    return tMatrix


row, column = input().split()
matrix = [[None]*int(column)] * int(row)
for x in range(int(row)):
    matrix[x] = [int(x) for x in input().split()]
transMatrix = transposeMatrix(matrix, int(row), int(column))
for r in transMatrix:
    for c in r:
        print(c, end=" ")
    print()


# Matrix Transposition
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Output:
# 1 4 7
# 2 5 8
# 3 6 9
#
# Input Format
#
# Input contains rowCount,colCount and the array values
#
# Constraints
#
# 1 ≤ array_size ≤ 1000
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 3 3
# 1 2 3
# 4 6 7
# 8 9 11
# Sample Output 0
#
# 1 4 8
# 2 6 9
# 3 7 11
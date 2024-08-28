def rotateMatrix(matrixx: list, r: int, c: int, flag: int) -> list:
    rMatrix = [None] * c
    for idx, val in enumerate(rMatrix):
        rMatrix[idx] = [None] * r
    for cIdx in range(c):
        for rIdx in range(r):
                rMatrix[cIdx][rIdx] = matrixx[r-1-rIdx][cIdx] if flag == 1 else matrixx[rIdx][c-1-cIdx]
    return rMatrix


row, column, flag = input().split()
matrix = [[None]*int(column)] * int(row)
for x in range(int(row)):
    matrix[x] = [int(x) for x in input().split()]
rotatedMatrix = rotateMatrix(matrix, int(row), int(column), int(flag))
for r in rotatedMatrix:
    for c in r:
        print(c, end=" ")
    print()

# Write a program to rotate a matrix in 90 degree.
# Case 1:
# Flag = 1
# Input:
# 2 3 1
# 4 6 3
# 5 4 2
# Output: 5 4 2
# 4 6 3
# 2 3 1
# Case 2:
# Flag = 0
# Input:
# 2 1
# 3 4
# Output:
# 1 4
# 2 3
#
# Input Format
#
# Input contains rowCount , columnCount, flag value and the array value
#
# Constraints
#
# 1 ≤ array_size ≤ 1000
#
# Output Format
#
# print the rotated array
#
# Sample Input 0
#
# 3 3 1
# 2 3 1
# 4 6 3
# 5 4 2
# Sample Output 0
#
# 5 4 2
# 4 6 3
# 2 3 1
# Sample Input 1
#
# 2 2 0
# 2 1
# 3 4
# Sample Output 1
#
# 1 4
# 2 3
def findPos(matrixL: list, mSize: int, num: int) -> str:
    for idx, val in enumerate(matrixL):
        for idx_i, val_i in enumerate(val):
            if num == val_i:
                return f"{idx}, {idx_i}"
    return "Not Found"


matrixSize = int(input())
matrixList = [[None]*matrixSize] * matrixSize
for m_idx, m_val in enumerate(matrixList):
    matrixList[m_idx] = [int(x) for x in input().split()]
n = int(input())
print(findPos(matrixList, matrixSize, n))

# Given an n x n matrix and a number x, find position of x in the matrix if it is present in it. Else print “Not Found”. In the given matrix, every row and column is sorted in increasing order
#
# Input Format
#
# Input contains the matrix size and the value to find
#
# Constraints
#
# Do not use static array
#
# Output Format
#
# print the position if found , else print Not Found
#
# Sample Input 0
#
# 4
# 10 20 30 40
# 15 25 35 45
# 27 29 37 48
# 32 33 39 50
# 29
# Sample Output 0
#
# 2,1

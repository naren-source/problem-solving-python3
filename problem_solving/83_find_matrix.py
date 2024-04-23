def findInMatrix(matrixList: list, r: int, c: int, k: int) -> str:
    for rIdx, rVal in enumerate(matrixList):
        for cIdx, cVal in enumerate(rVal):
            if cVal == k:
                return f"{rIdx} {cIdx}"
    return "-1 -1"


row, col = input().split()
matrixx = [[None]*int(col)] * int(row)
for x in range(int(row)):
    matrixx[x] = [int(x) for x in input().split()]
key = int(input())
print(findInMatrix(matrixx, int(row), int(col), key))

# Find a target value in a two-dimensional matrix given the number of rows as rowCount and number of columns as columnCount, and return its coordinates. If the value didn't exist, the program had to return (-1,-1).
#
# Input Format
#
# Input contains rowCount , columnCount, values and the target value
#
# Constraints
#
# 1 ≤ array_size ≤ 1000
#
# Output Format
#
# If the value didn't exist, print -1 -1 else print its coordinates
#
# Sample Input 0
#
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 7
# Sample Output 0
#
# 1 2

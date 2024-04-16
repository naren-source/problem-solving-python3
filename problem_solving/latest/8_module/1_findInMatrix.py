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


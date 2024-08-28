def cellCompete(cellList: list, day: int) -> None:
    cellListLength = len(cellList)
    while not day == 0:
        prevState = 0
        for cIdx in range(cellListLength):
            left = 0 if cIdx == 0 else prevState
            right = 0 if cIdx == (cellListLength - 1) else cellList[cIdx+1]
            prevState = cellList[cIdx]
            if left == right:
                cellList[cIdx] = 0
            else:
                cellList[cIdx] = 1
        day -= 1


cList = [int(x) for x in input().split()]
days = int(input())
cellCompete(cList, days)
for x in cList:
    print(x, end=" ")

# There is a colony of 8 cells arranged in a straight line where each day every cell competes with its adjacent cells(neighbour). Each day, for each cell, if its neighbours are both active or both inactive, the cell becomes inactive the next day, otherwise it becomes active the next day.
#
# Assumptions: The two cells on the ends have single adjacent cell, so the other adjacent cell can be assumed to be always inactive. Even after updating the cell state. consider its previous state for updating the state of other cells. Update the cell information of all cells simultaneously. Write a function cellCompete which takes takes one 8 element array of integers cells representing the current state of 8 cells and one integer days representing the number of days to simulate. An integer value of 1 represents an active cell and value of 0 represents an inactive cell.
#
# Input Format
#
# Input will have 8 array values and the no of days
#
# Constraints
#
# array size is 8 integers
#
# Output Format
#
# print the array
#
# Sample Input 0
#
# 1 0 0 0 0 1 0 0
# 1
# Sample Output 0
#
# 0 1 0 0 1 0 1 0

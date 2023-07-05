def find_max_ones(matrix):
    row_no = -1
    max_ones = 0
    for i in range(len(matrix)):
        count_ones = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count_ones += 1
        if count_ones > max_ones:
            row_no = i
            max_ones = count_ones
    return row_no


row, col = input().split()
matrix = [[0]*int(col)] * int(row)
for i in range(int(row)):
    matrix[i] = [int(x) for x in input().split()]
print(find_max_ones(matrix))

# # Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
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
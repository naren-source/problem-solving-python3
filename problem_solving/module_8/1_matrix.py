def find_in_matrix(matrix, find: int)->None:
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == find:
                print(f"{i},{j}")
                return
    print("Not Found")


size = int(input())
matrix = [[0]*size] * size
for i in range(size):
    matrix[i] = [int(x) for x in input().split()]
find = int(input())
find_in_matrix(matrix, find)


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
# Sample Input 1
#
# 4
# 10 20 30 40
# 15 25 35 45
# 27 29 37 48
# 32 33 39 50
# 100
# Sample Output 1
#
# Not Found
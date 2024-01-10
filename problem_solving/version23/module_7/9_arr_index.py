def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def reorder_arr_index(arr, index):
    for x in range(len(arr)):
        idx = x
        value = index[x]
        swap(arr, idx, value)
        swap(index, idx, value)


size = int(input())
arr = [int(x) for x in input().split()]
index = [int(x) for x in input().split()]
reorder_arr_index(arr, index)
for x in arr:
    print(x, end="  ")
print()
for x in index:
    print(x, end="  ")

# Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according to given index array.
#
# Input Format
#
# First line contains the no of elements for array second line contains the array valuies & index arrray values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the altered array and the ordered index array. use tab for space
#
# Sample Input 0
#
# 3
# 10    11    12
# 1    0    2
# Sample Output 0
#
# 11    10    12
# 0    1    2
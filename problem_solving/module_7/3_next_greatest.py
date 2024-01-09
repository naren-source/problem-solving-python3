def find_greatest(num_list, index):
    len_num_list = len(num_list)
    if index == (len_num_list-1): return -1
    max_num = num_list[index+1]
    for i in range(index+1, len_num_list):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num


def next_greatest(num_list):
    for idx, i in enumerate(num_list):
        greatest = find_greatest(num_list, idx)
        num_list[idx] = greatest


size = int(input())
num_list = [int(x) for x in input().split()]
next_greatest(num_list)
for x in num_list:
    print(x, end=" ")


# Given an array of integers, replace every element with the next greatest element (greatest element on the right side) in the array. Since there is no element next to the last element, replace it with -1. For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
#
# Input Format
#
# Input contains the arraysize & values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the altered array
#
# Sample Input 0
#
# 18
# 26 75 37 29 8 -67 31 42 72 57 -89 45 32 61 -64 25  48 -94
# Sample Output 0
#
# 75 72 72 72 72 72 72 72 61 61 61 61 61 48 48 48 -94 -1
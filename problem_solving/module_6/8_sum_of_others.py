def sum_of_others(list_items: list) -> list:
    result_list = [0] * len(list_items)
    for idx_i, i in enumerate(list_items):
        sum_o = 0
        for idx_j, j in enumerate(list_items):
            if idx_j != idx_i:
                sum_o += j
        result_list[idx_i] = sum_o
    return result_list


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
result_list = sum_of_others(input_list)
for i in result_list:
    print(i, end=" ")



# ===============================================

# Write a program to replace every element with sum of all other elements
#
# Input Format
#
# Each line contains the array size & values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# Output Format
#
# print the array
#
# Sample Input 0
#
# 5
# 12 34 56 76 87
# Sample Output 0
#
# 253 231 209 189 178
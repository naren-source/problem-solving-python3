def sum_of_right_elements(list_items: list) -> list:
    for idx_i, _ in enumerate(list_items):
        right_sum = 0
        for idx_j, j in enumerate(list_items):
            if idx_j > idx_i:
                right_sum += j
        list_items[idx_i] = right_sum
    return list_items


size_of_list = int(input())
input_list = [0] * size_of_list
input_list = [int(x) for x in input().split()]
right_sum_list = sum_of_right_elements(input_list)
for i in right_sum_list:
    print(i, end=" ")


# =======================================================
# Write a program to replace every element with sum of its right side elements
#
# Input Format
#
# Input will be the size and the values
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the altered array
#
# Sample Input 0
#
# 10
# 90 -60 78 12 76 61 -53 49 -6 -93
# Sample Output 0
#
# 64 124 46 34 -42 -103 -50 -99 -93 0

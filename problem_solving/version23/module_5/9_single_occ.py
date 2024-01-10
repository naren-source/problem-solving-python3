def unique_element(list_items: list) -> int:
    for idx_i, i in enumerate(list_items):
        unique = True
        for idx_j, j in enumerate(list_items):
            if i == j and idx_i != idx_j:
                unique = False
                break
        if unique: return i


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
print(unique_element(input_list))

# ===================================================
# Write a program to print the unique element in the array where every element will appear twice
#
# Input Format
#
# Input will have size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the unique element
#
# Sample Input 0
#
# 19
# 335 2 45 85 163 177 335 177 2 548 429 548 716 904 45 85 163 716 904
# Sample Output 0
#
# 429

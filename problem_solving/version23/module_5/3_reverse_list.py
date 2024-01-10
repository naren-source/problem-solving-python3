def swap_items(list_items: list, index: int):
    temp = list_items[index]
    list_items[index] = list_items[len(list_items)-1-index]
    list_items[len(list_items)-1-index] = temp


def reverse_list(list_items: list) -> list:
    for idx_i, _ in enumerate(list_items):
        if idx_i < (len(list_items) / 2):
            swap_items(list_items, idx_i)
    return list_items


size_of_list = int(input())
input_list = [0] * size_of_list
input_list = [int(x) for x in input().split()]
rev_list = reverse_list(input_list)
for i in rev_list:
    print(i, end=" ")


# ==================================================================
# Write a program to reverse the given array
#
# Input Format
#
# Input will be the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 10
# 825 573 380 192 150 691 219 353 2 6
# Sample Output 0
#
# 6 2 353 219 691 150 192 380 573 825

def swap_alternate(list_items: list) -> list:
    flag = True
    for idx, _ in enumerate(list_items):
        if flag and (idx != len(list_items)-1):
            temp = list_items[idx]
            list_items[idx] = list_items[idx+1]
            list_items[idx+1] = temp
        flag = not flag
    return list_items


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
return_list = swap_alternate(input_list)
for i in return_list:
    print(i, end=" ")


# ========================================================
# Swap Alternate Elements Write a program to swap alternate elements in an array
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
# 15
# 83 51 75 47 67 72 2 86 22 82 4 86 19 50 35
# Sample Output 0
#
# 51 83 47 75 72 67 86 2 82 22 86 4 50 19 35

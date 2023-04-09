def bubble_sort(list_items: list) -> list:
    for i, _ in enumerate(list_items):
        for j, _ in enumerate(list_items):
            if j == (len(list_items) -1 -i): break
            if list_items[j] > list_items[j+1]:
                temp = list_items[j+1]
                list_items[j+1] = list_items[j]
                list_items[j] = temp
    return list_items


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
return_list = bubble_sort(input_list)
for i in input_list:
    print(i, end=" ")


# ============================================================
# Write a program to implement a bubble sort
#
# Input Format
#
# Input is the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the sorted elements
#
# Sample Input 0
#
# 10
# 837 635 354 667 956 109  434 599 913  983
# Sample Output 0
#
# 109 354 434 599 635 667 837 913 956 983

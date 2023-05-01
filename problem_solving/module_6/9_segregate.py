def shift_right(list_items: list, start: int, end: int):
    iterations = end - start
    for itr in range(iterations):
        list_items[end - itr] = list_items[end - itr - 1]


def segregate_list(list_items: list) -> list:
    insert_pos = 0
    zero_pos = -1
    for idx, i in enumerate(list_items):
        if i == 0:
            zero_pos = idx
        if i < 0:
            if insert_pos != idx:
                shift_right(list_items, insert_pos, idx)
                list_items[insert_pos] = i
                if zero_pos != -1 and (insert_pos < zero_pos < idx):
                    zero_pos += 1
            insert_pos += 1
    if zero_pos != -1:
        shift_right(list_items, insert_pos, zero_pos)
        list_items[insert_pos] = 0
    return list_items


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
result_list = segregate_list(input_list)
for item in result_list:
    print(item, end=" ")


# ====================================
# Given an array that has positive numbers and negative numbers and zero in it. You need to separate the negative numbers and positive numbers in such a way that negative numbers lies to left of zero and positive numbers to the right and the original order of elements should be maintained.
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
# print the altered array
#
# Sample Input 0
#
# 5
# 98 -54 122 87 0
# Sample Output 0
# -2 3 -4 1 5
# -54 0 98 122 87

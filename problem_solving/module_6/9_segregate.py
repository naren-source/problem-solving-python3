def shift_right(list_items: list, start: int, end: int):
    print(list_items, start, end)
    for i in range(start, end):
        print("shift ", i)
        list_items[end - i] = list_items[end - i - 1]
    print(list_items)


def segregate_list(list_items: list) -> list:
    insert_pos = 0
    for idx, i in enumerate(list_items):
        if i < 0:
            print("i", i)
            if insert_pos != idx:
                shift_right(list_items, insert_pos, idx)
                list_items[insert_pos] = i
            insert_pos += 1
            print(list_items)

    return list_items


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
result_list = segregate_list(input_list)
for i in result_list:
    print(i, end=" ")


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
import sys


def second_max_one_itr(list_items: list) -> int:
    max = second_max = ~sys.maxsize
    for i in list_items:
        if i > max:
            second_max = max
            max = i
        elif i > second_max and i != max:
            second_max = i
    return second_max


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
print(second_max_one_itr(input_list))

# 1 2 3 4 5
# 5 4 3 2 1
# =====================================================

# Find 2nd maximum element in a given array in one iteration.
#
# Input Format
#
# Each line contains the array size & values
#
# Constraints
#
# 1 ≤ array_size ≤ 10000
#
# only one traversal
#
# Output Format
#
# print the second max
#
# Sample Input 0
#
# 5
# 98 -54 122 87 0
# Sample Output 0
#
# 98
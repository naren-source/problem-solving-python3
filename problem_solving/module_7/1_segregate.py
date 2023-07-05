from typing import List


def shift_right(num_list, pos):
    for idx in range(pos+1):
        num_list[pos - idx] = num_list[pos - idx-1]
    num_list[0] = 0


def segregate_num(num_list: List[int]) -> List[int]:
    for idx_i, i in enumerate(num_list):
        if i < 1 and idx_i != 0 :
            shift_right(num_list, idx_i)
    return num_list


list_size = int(input())
num_list = [int(x) for x in input().split()]
segregate_num(num_list)
for i in num_list:
    print(i, end=" ")

# You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
#
# Input Format
#
# Input will have array elements
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
# 6
# 0 1 0 1 1 1
# Sample Output 0
#
# 0 0 1 1 1 1

from typing import List


def shift_right(num_list: List[int], insert_position:int, current_position:int) -> None:
    num = num_list[current_position]
    for idx in range(current_position-insert_position):
        num_list[current_position - idx] = num_list[current_position - idx-1]
    num_list[insert_position] = num


def segregate_even_odd(num_list: List[int]) -> List[int]:
    even_ins_pos = 0
    for idx, i in enumerate(num_list):
        if i % 2 == 0:
            if idx != even_ins_pos:
                shift_right(num_list, even_ins_pos, idx)
            even_ins_pos += 1
    return num_list


list_size = int(input())
num_list = [int(x) for x in input().split()]
segregate_even_odd(num_list)
for i in num_list:
    print(i, end=" ")


# Given an array A[], write a 'C' program to segregates even and odd numbers. The ouput should have all even numbers first, and then odd numbers.
#
# Input Format
#
# Input contains the array values
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
# 7
# 12 34 45 9 8 90 3
# Sample Output 0
#
# 12 34 8 90 45 9 3
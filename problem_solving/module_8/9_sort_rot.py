def shift_left(num_list, position):
    for x in range(position+1):
        temp = num_list[0]
        for y in range(len(num_list)-1):
            num_list[y] = num_list[y+1]
        num_list[len(num_list)-1] = temp


def find_min(num_list):
    length = len(num_list)
    for x in range(length-1):
        if not ((num_list[x] - num_list[x+1] == 1) or (num_list[x] - num_list[x+1] == -1)):
            shift_left(num_list, x)
            break
    return num_list[0] if num_list[0]< num_list[length-1] else num_list[length-1]


size = int(input())
num_list = [int(x) for x in input().split()]
print(find_min(num_list))


# A sorted array is rotated at some unknown point, find the minimum element in it.
#
# Following solution assumes that all elements are distinct.
#
# Examples
#
# Input: {5, 6, 1, 2, 3, 4} Output: 1
#
# Input: {1, 2, 3, 4} Output: 1
#
# Input: {2, 1} Output: 1
#
# Input Format
#
# Input contains size and the values
#
# Constraints
#
# NIL
#
# Output Format
#
# Print the minimum element
#
# Sample Input 0
#
# 6
# 5 6 1 2 3 4
# Sample Output 0
#
# 1
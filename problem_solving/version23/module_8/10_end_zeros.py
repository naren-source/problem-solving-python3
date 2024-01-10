def shift_left(num_list, start, rotations):
    for x in range(rotations):
        for y in range(start, len(num_list)-1):
            num_list[y] = num_list[y+1]
        num_list[len(num_list)-1] = 0


def shift_zeros(num_list):
    length = len(num_list)
    for x in range(length):
        if num_list[x] == 0:
            for y in range(x, length):
                if num_list[y] != 0:
                    shift_left(num_list, x, y-x)
                    break


size = int(input())
num_list = [int(x) for x in input().split()]
shift_zeros(num_list)
for x in num_list:
    print(x, end=" ")


# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
#
# Input Format
#
# Input contains the size and values
#
# Constraints
#
# NIL
#
# Output Format
#
# Print the array
#
# Sample Input 0
#
# 11
# 1 9 8 4 0 0 2 7 0 6 0
# Sample Output 0
#
# 1 9 8 4 2 7 6 0 0 0 0
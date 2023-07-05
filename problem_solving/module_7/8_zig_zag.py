def zig_zag(num_list):
    for i in range(len(num_list)-1):
        if (i % 2 == 0 and num_list[i] > num_list[i+1]) or (i % 2 != 0 and num_list[i]<num_list[i+1]):
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp


size = int(input())
num_list = [int(x) for x in input().split()]
zig_zag(num_list)
for x in num_list:
    print(x, end=" ")


# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.
#
# Input Format
#
# Input contains the no of elements & array values
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
# 4 3 7 8 6 2 1
# Sample Output 0
#
# 3 7 4 8 2 6 1
def arr_to_index(num_list):
    new_arr = [0] * len(num_list)
    for i in range(len(num_list)):
        value = num_list[i]
        index = i
        new_arr[value] = index
    for x in new_arr:
        print(x, end=" ")


size = int(input())
num_list = [int(x) for x in input().split()]
arr_to_index(num_list)


# Given an array of size n where all elements are in range from 0 to n-1, change contents of arr[] so that arr[i] = j is changed to arr[j] = i.
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
# 4
# 1 3 0 2
# Sample Output 0
#
# 2 0 3 1
# Explanation 0
#
# Explanation for the above output. Since arr[0] is 1, arr[1] is changed to 0 Since arr[1] is 3, arr[3] is changed to 1 Since arr[2] is 0, arr[0] is changed to 2 Since arr[3] is 2, arr[2] is changed to 3
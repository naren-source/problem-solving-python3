def shift_right(arr, pos):
    length = len(arr)
    for i in range(length-1-pos):
        arr[length - 1 -i] = arr[length - 2 -i]


def sort_frequency(num_list):
    length = len(num_list)
    count_list = [0] * 10
    freq_order_list = [0] * 10
    for i in range(length):
        count = 0
        for j in range(length):
            if num_list[j] == num_list[i]:
                count += 1
        count_list[num_list[i]] = count
        for k in range(len(freq_order_list)):
            if count >= count_list[freq_order_list[k]]:
                shift_right(freq_order_list, k)
                freq_order_list[k] = num_list[i]
                break
    for i in range(length):
        count = count_list[freq_order_list[i]]
        for j in range(count):
            print(freq_order_list[i], end=" ")


size = int(input())
num_list = [int(x) for x in input().split()]
sort_frequency(num_list)


# Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
#
# Input Format
#
# Input contains the no of elements and array values
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
# 17
# 3 2 4 6 2 4 3 3 4 5 6 3 2 4 5 5 3
# Sample Output 0
#
# 3 3 3 3 3 4 4 4 4 2 2 2 5 5 5 6 6
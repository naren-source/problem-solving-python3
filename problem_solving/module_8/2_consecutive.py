def sort_list(num_list):
    length = len(num_list)
    for i in range(length):
        for j in range(length-i-1):
            if num_list[j]>num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp


def find_consecutive(num_list):
    sort_list(num_list)
    difference = 0
    for i in range(len(num_list)-1):
        difference += num_list[i+1] - num_list[i]

    if difference == len(num_list) - 1:
        return "Consecutive"
    else:
        return "Not Consecutive"


size = int(input())
num_list = [0] * size
num_list = [int(x) for x in input().split()]
print(find_consecutive(num_list))



# # Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.
#
# Examples: a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.
#
# b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.
#
# c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.
#
# d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.
#
# Input Format
#
# Input contains the no of elements and the elements
#
# Constraints
#
# Dynamic memory allocation
#
# Output Format
#
# Print Consecutive if the function returns true else print Not Consecutive
#
# Sample Input 0
#
# 5
# 5 2 3 1 4
# Sample Output 0
#
# Consecutive
# Sample Input 1
#
# 5
# 34 23 52 12 3
# Sample Output 1
#
# Not Consecutive
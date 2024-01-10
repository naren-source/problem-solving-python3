def sum_of_list(list_items: list) -> int:
    sum_of_items = 0
    for i in list_items:
        sum_of_items += i
    return sum_of_items


size_of_list = int(input())
list_items = [0] * size_of_list
list_items = [int(x) for x in input().split()]
print(sum_of_list(list_items))


# ==============================================
# Write a program to print the sum of the array
#
# Input Format
#
# Input will be the size of the array and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the sum
#
# Sample Input 0
#
# 10
# 90 -60 78 12 76 61 -53 49 -6 -93
# Sample Output 0
#
# 154

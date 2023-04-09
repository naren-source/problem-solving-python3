def sum_of_alternate_items(list_items: list) -> int:
    sum_of_items = 0
    flag = True
    for i in list_items:
        if flag:
            sum_of_items += i
        flag = not flag
    return sum_of_items


size_of_list = int(input())
list_items = [0] * size_of_list
list_items = [int(x) for x in input().split()]
print(sum_of_alternate_items(list_items))


# ==============================================
# Write a program to print the sum of alternate elements
#
# Input Format
#
# Input will be the size and the elements
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
# 825 573 380 192 150 691 219 353 2 6
# Sample Output 0
#
# 1576

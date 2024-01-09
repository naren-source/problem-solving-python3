def largest_three(num_list):
    length = len(num_list)
    for i in range(length):
        for j in range(length-i-1):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp


size = int(input())
num_list = [int(x) for x in input().split()]
largest_three(num_list)
for x in range(3):
    print(num_list[len(num_list)-1-x], end="")
    if not x==2:
        print("",end=", ")


# Given an array with all distinct elements, find the largest three elements.

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
# print the largest elements
#
# Sample Input 0
#
# 6
# 10 4 3 50 23 90
# Sample Output 0
#
# 90, 50, 23
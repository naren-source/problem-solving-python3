def mult_prev_next(num_list):
    length = len(num_list)
    for i in range(length):
        start = i if i <= 0 else i - 1
        end = i if i >= (len(num_list) - 1) else i + 1
        print(num_list[start] * num_list[end], end=" ")


size = int(input())
num_list = [int(x) for x in input().split()]
mult_prev_next(num_list)


# Given an array of integers, update every element with multiplication of previous and next elements with following exceptions. a) First element is replaced by multiplication of first and second. b) Last element is replaced by multiplication of last and second last.
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
# 5
# 2 3 4 5 6
# Sample Output 0
#
# 6 8 15 24 30
# Explanation 0
#
# // We get the above output using following // arr[] = {2*3, 2*4, 3*5, 4*6, 5*6}
def find_repeat(num_list):
    length = len(num_list)
    repeats = [0] * length
    for i in range(length):
        repeats[num_list[i]] += 1
        if repeats[num_list[i]] > 1:
            print(num_list[i])


size = int(input())
num_list = [int(x) for x in input().split()]
find_repeat(num_list)

# You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except two numbers which occur twice. Find the two repeating numbers.
#
# For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5
#
# The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.
#
# Input Format
#
# Input contains n and n+2 values
#
# Constraints
#
# Dynamic memory
#
# Output Format
#
# Print the repeated elements
#
# Sample Input 0
#
# 5
# 4 2 4 5 2 3 1
# Sample Output 0
#
# 4,2
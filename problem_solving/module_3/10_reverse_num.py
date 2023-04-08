def reverse_the_number(n: int) -> int:
    reversed_num = 0
    while n:
        r = n % 10
        reversed_num = (reversed_num * 10) + r
        n = int(n/10)
    return reversed_num


inputs = int(input())
for i in range(inputs):
    num = int(input())
    print(reverse_the_number(num))



# ======================================================================
# Write a 'C' Program to reverse the given number
#
# Input Format
#
# First line represents the test case and the following lines will have the integers to reverse
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# print the reversed value
#
# Sample Input 0
#
# 5
# 124
# 6783
# 34687
# 87956
# 678056
# Sample Output 0
#
# 421
# 3876
# 78643
# 65978
# 650876

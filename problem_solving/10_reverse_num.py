def reverseTheNum(num):
    result = 0
    while int(num) > 0:
        last = num % 10
        result = (result*10) + last
        num /= 10
        num = int(num)
    return result


numberOfInputs = int(input())
for i in range(numberOfInputs):
    n = int(input())
    print(reverseTheNum(n))



# Write a  Program to reverse the given number
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

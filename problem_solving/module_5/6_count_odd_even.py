def count_odd_even(list_items: list):
    odd = 0
    even = 0
    for i in list_items:
        n = int(i / 2)*2
        even += 1 if n == i else 0
        odd += 1 if n != i else 0
    print(f"{odd} {even}")


list_size = int(input())
input_list = [0] * list_size
input_list = [int(x) for x in input().split()]
count_odd_even(input_list)


# =======================================
# Write a program to count the odd and even no of elements
#
# Input Format
#
# Input will have the size and the elements
#
# Constraints
#
# 1<=size<=1000
#
# Output Format
#
# Print the odd count and then even count
#
# Sample Input 0
#
# 10
# 33 90 31 89 63 56 22 93 35 52
# Sample Output 0
#
# 6 4

def frequency_of_digits(n: int) -> list:
    frequency_list = [0] * 10
    while n:
        r = n % 10
        frequency_list[r] += 1
        n = int(n / 10)
    return frequency_list


for idx_i, i in enumerate(frequency_of_digits(int(input()))):
    print(f"Frequency of {idx_i} = {i}")


# -====================================================

# Write a 'C' program to print the frequency of digits in the given number
#
# Input Format
#
# Input is a number
#
# Constraints
#
# 1 ≤ num ≤ 100000000
#
# Output Format
#
# Frequency of 0 = __ Frequency of 1 = __
#
# Sample Input 0
#
# 46325642
# Sample Output 0
#
# Frequency of 0 = 0
# Frequency of 1 = 0
# Frequency of 2 = 2
# Frequency of 3 = 1
# Frequency of 4 = 2
# Frequency of 5 = 1
# Frequency of 6 = 2
# Frequency of 7 = 0
# Frequency of 8 = 0
# Frequency of 9 = 0

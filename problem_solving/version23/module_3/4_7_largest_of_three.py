def check_largest_or_smallest(num_list: list[int], check_type: str = "L") -> str:
    for idx_i, i in enumerate(num_list):
        for idx_j, j in enumerate(num_list):
            if (idx_j < len(num_list)-idx_i-1) and (num_list[idx_j] < num_list[idx_j+1] if check_type == "L" else num_list[idx_j] > num_list[idx_j+1]):
                temp = num_list[idx_j+1]
                num_list[idx_j+1] = num_list[idx_j]
                num_list[idx_j] = temp
    return_string = ""
    for idx_n, n in enumerate(num_list):
        return_string += str(n)
        if idx_n+1 != len(num_list):
            return_string += " > " if check_type == "L" else " < "
    return return_string


numberOfInputs = int(input())
for i in range(numberOfInputs):
    numList = [int(x) for x in input().split()]
    print(check_largest_or_smallest(numList))


#=============================================================
#Write a program to find the largest of three numbers?

# Input Format
#
# The first line informs you the number of test cases. Each separate line has three integer values to find the relation between the three integer values i.e. to find the largest of the three values
#
# Constraints
#
# -2147483647 ≤ n1,n2 ≤ 2147483647
#
# Output Format
#
# %d > %d > %d
#
# Sample Input 0
#
# 3
# 12 90 45
# 10 190 1234
# 1290 56 823
# Sample Output 0
#
# 90 > 45 > 12
# 1234 > 190 > 10
# 1290 > 823 > 56


# [2,6,1,3,5]
# [2,1,3,5,6]

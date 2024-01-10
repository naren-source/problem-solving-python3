def find_max_repeats(num_list, k):
    ref_arr = [0] * k
    for i in range(len(num_list)):
        ref_arr[num_list[i]] += 1
    maxi = 0
    for i in range(len(ref_arr)):
        if ref_arr[i]>maxi:
            maxi = i
    return maxi


n, k = input().split()
num_list = [int(x) for x in input().split()]
print(find_max_repeats(num_list, int(k)))


# Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n. Find the maximum repeating number in this array. For example, let k be 10 the given array be arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2. Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.
#
# Input Format
#
# Input contains size,k and the values
#`
# Constraints
#
# Dyanmic memory
#
# Output Format
#
# Print the value
#
# Sample Input 0
#
# 14 10
# 1 2 2 2 0 2 0 2 3 8 0 9 2 3
# Sample Output 0
#
# 2
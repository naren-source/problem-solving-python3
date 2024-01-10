def find_nbyk(num_list, n, k):
    limit = int(n / k)
    ref_arr = [0] * 10
    for i in range(n):
        ref_arr[num_list[i]] += 1
    count = 0
    for i in range(len(ref_arr)):
        if ref_arr[i] > limit:
            if count != 0: print(",",end="")
            print(i, end="")
            count += 1
    if count == 0:
        print("No such element")


n, k = input().split()
num_list = [int(x) for x in input().split()]
find_nbyk(num_list, int(n), int(k))

# Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3.
#
# Input Format
#
# Input contains size n , k and the values
#
# Constraints
#
# NIL
#
# Output Format
#
# print the value else print No such element
#
# Sample Input 0
#
# 8 4
# 3 1 2 2 1 2 3 3
# Sample Output 0
#
# 2,3
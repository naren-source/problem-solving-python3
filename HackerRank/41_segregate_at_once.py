def numSegregation(numList: list) -> None:
    left = -1
    right = -1
    for idx, val in enumerate(numList):
        if numList[idx] == 0:
            left = idx
        elif numList[idx] == 1 and right == -1:
            right = idx
        if left > right and (left > -1 and right > -1):
            numList[left] = 1
            numList[right] = 0
            left = right
            right += 1


listSize = int(input())
nList = [int(x) for x in input().split()]
numSegregation(nList)
for x in nList:
    print(x, end=" ")


# You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
#
# Input Format
#
# Input will have array elements
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
# 6
# 0 1 0 1 1 1
# Sample Output 0
#
# 0 0 1 1 1 1

# def segregate0and1(arr, size):
#     # Initialize left and right indexes
#     left, right = 0, size-1
#
#     while left < right:
#         # Increment left index while we see 0 at left
#         while arr[left] == 0 and left < right:
#             left += 1
#
#         # Decrement right index while we see 1 at right
#         while arr[right] == 1 and left < right:
#             right -= 1
#
#         # If left is smaller than right then there is a 1 at left
#         # and a 0 at right. Exchange arr[left] and arr[right]
#         if left < right:
#             arr[left] = 0
#             arr[right] = 1
#             left += 1
#             right -= 1
#
#     return arr
#
# # driver program to test
# arr = [0, 1, 0, 1, 1, 1]
# arr_size = len(arr)
# print("Array after segregation")
# print(segregate0and1(arr, arr_size))

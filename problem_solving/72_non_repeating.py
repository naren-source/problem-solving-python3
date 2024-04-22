def nonRepeating(listOne: list, sizeOne: int, listTwo: list, sizeTwo: int) -> None:
    resultList = []
    for x in listOne:
        if not ((x in listTwo) and (x in listOne)):
            resultList.append(x)

    for x in listTwo:
        if not ((x in listOne) and (x in listTwo)):
            resultList.append(x)


    for idx, val in enumerate(resultList):
        if idx == 0:
            print("{", end="")
            print(f"{val}", end=",")
        elif idx == len(resultList)-1:
            print(val, end="}")
        else:
            print(val, end=",")
    print(f" Total is {len(resultList)}")


testCase = int(input())
for tc in range(testCase):
    listOneSize, listTwoSize = input().split()
    nListOne = [int(x) for x in input().split()]
    nListTwo = [int(x) for x in input().split()]
    nonRepeating(nListOne, int(listOneSize), nListTwo, int(listOneSize))

# Eliminate repeated elements in Array. Printing non repeating elements in array and printing the total. Arr1 = {1,2,3,4,5} Len1 = 5 Arr 2 = {2,6,8,10} Len2 = 4 Output = {1,3,4,5,6,8,10} Total is 7.
#
# Input Format
#
# The first line informs you the number of test cases. Each test case will have the size of two arrays and the values in the next lines.
#
# Constraints
#
# 1 ≤ n ≤105
#
# 1 ≤ values ≤ 109
#
# Output Format
#
# Print non repeating elements in { } and the count
#
# Sample Input 0
#
# 3
# 5 6
# 34 89 12 45 93
# 12 93 45 23 78 35
# 10 3
# 9058 364 986 23 98 123 546 908 675 53
# 23 53 98
# 6 7
# 23 364 98 234 79 244
# 67 56 34 87 98 73 21
# Sample Output 0
#
# {34,89,23,78,35} Total is 5
# {9058,364,986,123,546,908,675} Total is 7
# {23,364,234,79,244,67,56,34,87,73,21} Total is 11

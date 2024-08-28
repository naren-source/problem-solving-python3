def lessThanKey(nList: list, lSize: int, key: int) -> int:
    count = 0
    for x in nList:
        if x < key:
            count += 1
    return count


testCase = int(input())
for tc in range(testCase):
    listSize, key = input().split()
    nList = [int(x) for x in input().split()]
    print(lessThanKey(nList, int(listSize), int(key)))


# Print and count all the numbers which are less than a given key element from a given array.
#
# Input Format
#
# The first line informs you the number of test cases. Every test cases have two lines one for n ( array size ) and key , and the another line has the array values.
#
# Constraints
#
# 1 ≤ n ≤105
#
# 1 ≤ key ≤ 109
#
# Output Format
#
# Print the count
#
# Sample Input 0
#
# 3
# 5 56
# 34 89 12 45 93
# 10 163
# 9058 364 986 23 98 123 546 908 675 53
# 7 12
# 67 56 34 87 98 73 21
# Sample Output 0
#
# 3
# 4
# 0

def isOccured(num1: int, num2: int) -> int:
    count = 0
    while num1:
        r = num1 % 10
        if r == num2:
            count += 1
        num1 = int(num1 / 10)
    return count


testCase = int(input())
for tc in range(testCase):
    n1, n2 = input().split()
    print(isOccured(int(n1), int(n2)))

# Input: num1 and num2 such that 0 <= num1 <= 99999999 and 0 <= num2 <=9. You have to find number of occurences of input num2 in input num1 and return it with function int isOccured(int num1, int num2).
#
# Input Format
#
# First line indicates the number of test cases. Next lines will have num1 and num2
#
# Constraints
#
# 0 ≤ num1 ≤ 99999999
#
# 0 ≤ num2 ≤ 9
#
# Output Format
#
# print the count
#
# Sample Input 0
#
# 3
# 199294 9
# 1222212 2
# 1001010 0
# Sample Output 0
#
# 3
# 5
# 4

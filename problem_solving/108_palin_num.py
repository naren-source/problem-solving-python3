def reverseNum(num: int) -> int:
    reverse = 0
    while num:
        r = num % 10
        reverse = reverse*10 + r
        num = int(num/10)
    return reverse


def checkPalindrome(n: int) -> int:
    maxLimit = 5
    while maxLimit:
        sum = n + reverseNum(n)
        reverseSum = reverseNum(sum)
        if sum == reverseSum:
            return sum
        n = sum
        maxLimit -= 1
    return -1


print(checkPalindrome(int(input())))

# Given a number, reverse it and add it to itself unless it becomes a palindrome or the the count becomes 5 times. If it becomes a palindrome then print that palindrome number, otherwise print -1
#
# Ex: 23 32 => 55
#
# Input Format
#
# Input contains the number
#
# Constraints
#
# 1 ≤ N ≤ 1000
#
# Output Format
#
# print the palindrome number or -1
#
# Sample Input 0
#
# 23
# Sample Output 0
#
# 55

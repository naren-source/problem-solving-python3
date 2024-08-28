def reverseWordsinStr(sList: list) -> str:
    left = 0
    right = len(sList) - 1
    while left < right:
        temp = sList[left]
        sList[left] = sList[right]
        sList[right] = temp
        left += 1
        right -= 1
    return " ".join(sList)


cSize = int(input())
inputStr = input().split()
print(reverseWordsinStr(inputStr))


# Write a program to reverse the word in a given string ? I/P : ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT O/P EIGHT SEVEN SIX FIVE FOUR THREE TWO ONE
#
# Input Format
#
# First line denotes the length of the string Next line denotes the string
#
# Constraints
#
# Change the original string
#
# Output Format
#
# print the reversed string
#
# Sample Input 0
#
# 23
# This is a test sentence
# Sample Output 0
#
# sentence test a is This
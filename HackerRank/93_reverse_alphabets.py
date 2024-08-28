def reverseThis(word: str) -> str:
    word = [*word]
    wordLen = len(word)
    start = 0
    end = wordLen-1
    while start < end:
        if not (65 <= ord(word[start]) <= 90 or 97 <= ord(word[start]) <= 122):
            start += 1
        elif not (65 <= ord(word[end]) <= 90 or 97 <= ord(word[end]) <= 122):
            end -= 1
        else:
            temp = word[start]
            word[start] = word[end]
            word[end] = temp
            start += 1
            end -= 1
    return "".join(word)


def reverseWords(sList: list) -> list:
    for x in range(len(sList)):
        sList[x] = reverseThis(sList[x])
    return sList


sLen = int(input())
inputStrList = input().split()
inputStrList = reverseWords(inputStrList)
for x in inputStrList:
    print(x, end=" ")


# Write a program to reverse the words in a given string, leave non-alphabet characters and numeric digits undisturbed. I/P This is fun, hopefully. O/P sihT si nuf, yllufepoh.
#
# Input Format
#
# First line represents the string length Next line will have the string
#
# Constraints
#
# Change the original string
#
# Output Format
#
# print the altered string
#
# Sample Input 0
#
# 23
# This is fun, hopefully.
# Sample Output 0
#
# sihT si nuf, yllufepoh.

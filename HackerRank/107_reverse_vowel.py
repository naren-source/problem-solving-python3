def checkIfVowel(ch: str) -> bool:
    vowelList = ['a', 'e', 'i', 'o', 'u']
    # for x in vowelList:
    #     if x == ch:
    #         return True
    # return False
    return ch in vowelList


def reverseVows(iStr: str) -> str:
    cStr = [*iStr]
    left = 0
    right = len(cStr) - 1
    while left < right:
        while not checkIfVowel(cStr[left]):
            left += 1
        while not checkIfVowel(cStr[right]):
            right -= 1
        if left < right:
            temp = cStr[left]
            cStr[left] = cStr[right]
            cStr[right] = temp
            left += 1
            right -= 1

    return "".join(cStr)


print(reverseVows(input()))


# Given a string, reverse only the vowels present in it and print the resulting string
#
# Input Format
#
# Input contains the string
#
# Constraints
#
# 1 ≤ string length ≤ 10 4
#
# Output Format
#
# print the altered string
#
# Sample Input 0
#
# practice
# Sample Output 0
#
# prectica

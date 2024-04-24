def rotateStr(rString: str, rLength: int) -> str:
    charList = [*rString]
    tempCh = charList[0]
    for ch in range(rLength-1):
        charList[ch] = charList[ch+1]
    charList[rLength-1] = tempCh
    return "".join(charList)


def checkStrEquality(oStr: str, rStr: str) -> int:
    rLen = len(rStr)
    rLenLoop = rLen
    while not rLenLoop == 0:
        if rStr == oStr:
            return 1
        rStr = rotateStr(rStr, rLen)
        rLenLoop -= 1
    return -1


orgString = input()
rotatedString = input()
print(checkStrEquality(orgString, rotatedString))


# Program to rotate a given string. If 2 strings are equal then print 1 else print -1.
# Given 2 strings.
# Ip: sample
# mplesa
# Op: 1
# Ip: sample
# mplase
# Op:-1
# Ip: abc
# cba
# Op: 1
# Ip: ab
# Aa
# Op: -1
#
# Input Format
#
# Input contains two strings
#
# Constraints
#
# 1 ≤ string_length ≤ 1000
#
# Output Format
#
# If 2 strings are equal then print 1 else print -1
#
# Sample Input 0
#
# sample
# mplesa
# Sample Output 0

1
def checkSubs(mIdx: int, mStr: str, sStr: str) -> int:
    for s in range(len(sStr)):
        if not mStr[s+mIdx] == sStr[s]:
            return 0
    return 1


def checkOccurance(mStr: str, sStr: str) -> int:
    occurance = 0
    for m in range(len(mStr)-len(sStr)+1):
        if mStr[m] == sStr[0]:
            occurance += checkSubs(m, mStr, sStr)
    return occurance


mainString = input()
subString = input()
print(checkOccurance(mainString, subString))


# Find the occurance of a substring in a parent string
# Input : aAbcDefabcAdf
# Substring : abc
# Output : 1
#
# Input Format
#
# Input contains string and the substring
#
# Constraints
#
# 1 ≤ string_length ≤ 1000
#
# 1 ≤ substring_length ≤ 100
#
# Output Format
#
# print the count
#
# Sample Input 0
#
# aAbcDefabcAdf
# abc
# Sample Output 0
#
# 1
def removeSpace(lPos, rPos, inputStr) -> str:
    strList = [*inputStr]
    strResult = ""
    for x in range(len(inputStr)-rPos):
        strList[lPos+x] = strList[rPos+x]
    return strResult.join(strList)


def removeExtraSpace(iStr: str) -> str:
    right = 1
    left = right - 1
    loopTime = len(iStr)
    while True:
        if iStr[left] == " ":
            if iStr[right] == " ":
                right += 1
            else:
                if right-left > 1:
                    iStr = removeSpace(left + 1, right, iStr)
                    loopTime = loopTime - (right - left - 1)
                    right = left + 1
                else:
                    left += 1
                    right += 1
        else:
            left += 1
            right += 1

        if right == loopTime-1:
            resultStr = ""
            for x in range(loopTime):
                resultStr += iStr[x]
            iStr = resultStr
            break

    return iStr


print(removeExtraSpace(input()))

# Write a program to remove all the extra spaces from the given string
#
# Input Format
#
# Given a string
#
# Constraints
#
# 1<=length<=1000 only one space is allowed for each word
#
# Output Format
#
# Print the string with no extra spaces
#
# Sample Input 0
#
# TqdvNiH UuJppK        zRCDppt     tKbQjwu     VPCDpqK        LbGSMx
# Sample Output 0
#
# TqdvNiH UuJppK zRCDppt tKbQjwu VPCDpqK LbGSMx
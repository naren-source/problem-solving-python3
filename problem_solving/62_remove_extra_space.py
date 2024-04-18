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

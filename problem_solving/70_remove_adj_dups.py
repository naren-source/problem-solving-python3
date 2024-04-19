def leftShift(lPos: int, rPos: int, inputStr: str) -> str:
    strList = [*inputStr]
    strResult = ""
    for x in range(len(inputStr) - rPos):
        strList[lPos + x] = strList[rPos + x]
    return strResult.join(strList)

def removeAdjacentDuplicates(iStr: str) -> str:
    left = 0
    right = left + 1
    loopTime = len(iStr)
    strLen = loopTime
    while True:
        if iStr[left] == iStr[right]:
            right += 1
        else:
            if right - left > 1:
                iStr = leftShift(left, right, iStr)
                loopTime = loopTime - (right-left)
                left -= 1
                right = left + 1
            else:
                left += 1
                right += 1
        if right == loopTime:
            if loopTime == 1:
                return "NILL"
            if loopTime == strLen:
                return iStr
            break
    resultStr = ""
    for x in range(loopTime):
        resultStr += iStr[x]
    return resultStr


print(removeAdjacentDuplicates(input()))

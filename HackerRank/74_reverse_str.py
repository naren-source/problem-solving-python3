def reverseString(iStr: str, sSize: int) -> str:
    loopTime = int(sSize/2) if (sSize % 2 == 0) else (int(sSize/2) - 1)
    iStr = [*iStr]
    for x in range(loopTime):
        temp = iStr[x]
        iStr[x] = iStr[sSize-x]
        iStr[sSize - x] = temp
    resultStr = ""
    iStr[0] = ""
    return resultStr.join(iStr)


testCase = int(input())
for tc in range(testCase):
    strSize, *strlist = input().split()
    strInput = ""
    for x in strlist:
        strInput += (x + " ")
    print(reverseString(strInput, int(strSize)))


# Write a Program to reverse the given string.
#
# Input Format
#
# First line informs you the number of test cases. The following lines contain the string length and the string
#
# Constraints
#
# 1 ≤ t ≤ 10
#
# 1 ≤ length ≤ 1000000
#
# Do not use extra space Alter the original Do not use in-built functions
#
# Output Format
#
# print the reversed string
#
# Sample Input 0
#
# 3
# 134 Aesops fable of the Tortoise and the Hare. When a wolf really does come, no one believes him. a lion is eating all the forest animals.
# 69 children not to underestimate themselves.a man tries to rescue a cat.
# 65 Little readers learn to overcome bad habits with The Wise Old Man
# Sample Output 0
#
# .slamina tserof eht lla gnitae si noil a .mih seveileb eno on ,emoc seod yllaer flow a nehW .eraH eht dna esiotroT eht fo elbaf sposeA
# .tac a eucser ot seirt nam a.sevlesmeht etamitserednu ot ton nerdlihc
# naM dlO esiW ehT htiw stibah dab emocrevo ot nrael sredaer elttiL
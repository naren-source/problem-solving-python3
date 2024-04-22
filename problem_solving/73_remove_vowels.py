def leftShift(inputStr: str, ctr: int, strSize: int) -> str:
    charList = [*inputStr]
    for idx in range(ctr, strSize-1):
        charList[idx] = charList[idx + 1]
    charList[strSize-1] = ""
    resultStr = ""
    return resultStr.join(charList)


def removeVowels(iStr: str, sSize: int) -> str:
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    while counter < sSize:
        if iStr[counter].lower() in vowelsList:
            iStr = leftShift(iStr, counter, sSize)
            sSize -= 1
        else:
            counter += 1
        if counter == sSize:
            return iStr


testCase = int(input())
for tc in range(testCase):
    strSize, *strlist = input().split()
    strInput = ""
    for x in strlist:
        strInput += (x + " ")
    print(removeVowels(strInput, int(strSize)))


# Write a program to remove vowels from the given string
#
# Input Format
#
# First line contains the test cases. The following lines containthe length of the string and the string
#
# Constraints
#
# 1 ≤ length ≤ 1000000
#
# Change the original string . No extra space to alter the string. Do not use in-built string functions
#
# Output Format
#
# Print the altered string
#
# Sample Input 0
#
# 3
# 42 Aesop's fable of the Tortoise and the Hare
# 49 When a wolf really does come, no one believes him
# 39 a lion is eating all the forest animals
# Sample Output 0
#
# sp's fbl f th Trts nd th Hr
# Whn  wlf rlly ds cm, n n blvs hm
#  ln s tng ll th frst nmls